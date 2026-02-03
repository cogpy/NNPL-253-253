#!/usr/bin/env python3
"""
Extract pattern content from HTML files in apl/ directory and
complete the markdown files in markdown/apl/ directory.
"""

import re
import os
from pathlib import Path
from typing import Dict, Optional


def clean_html_text(text: str) -> str:
    """Remove HTML tags and clean up text."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&quot;', '"')
    text = text.replace('&amp;', '&')
    text = text.replace('&#8212;', '—')
    text = text.replace('<SUP>2</SUP>', '²')
    text = text.replace('<SUP>', '^')
    text = text.replace('</SUP>', '')
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def extract_pattern_from_html(html_path: str) -> Optional[Dict[str, str]]:
    """Extract pattern components from HTML file."""
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {html_path}: {e}")
        return None
    
    # Extract pattern number and title from title tag
    title_match = re.search(r'<TITLE>\s*(\d+)\s+([^<]+)</TITLE>', content, re.IGNORECASE)
    if not title_match:
        return None
    
    pattern_num = title_match.group(1)
    pattern_title = title_match.group(2).strip()
    
    # Extract the problem statement (bold text before "Therefore:")
    # Look for h3class content before "Therefore:"
    problem_pattern = r'<h3[^>]*>([^<]*)</h3>.*?<h3[^>]*>Therefore:</h3>'
    problem_match = re.search(problem_pattern, content, re.IGNORECASE | re.DOTALL)
    
    problem = ""
    if problem_match:
        problem = clean_html_text(problem_match.group(1))
    else:
        # Try alternate pattern
        problem_pattern = r'<span class=h3class>([^<]*)</span>.*?<span class=h3class>Therefore:</span>'
        problem_match = re.search(problem_pattern, content, re.IGNORECASE | re.DOTALL)
        if problem_match:
            problem = clean_html_text(problem_match.group(1))
    
    # Extract the solution statement (bold text after "Therefore:")
    solution_pattern = r'<h3[^>]*>Therefore:</h3>\s*<[^>]*>\s*<h3[^>]*>([^<]+(?:<[^>]+>[^<]*</[^>]+>[^<]*)*)</h3>'
    solution_match = re.search(solution_pattern, content, re.IGNORECASE | re.DOTALL)
    
    solution = ""
    if solution_match:
        solution = clean_html_text(solution_match.group(1))
    else:
        # Try alternate pattern
        solution_pattern = r'<span class=h3class>Therefore:</span>.*?<span class=h3class>([^<]+(?:<[^>]+>[^<]*</[^>]+>[^<]*)*)</span>'
        solution_match = re.search(solution_pattern, content, re.IGNORECASE | re.DOTALL)
        if solution_match:
            solution_text = solution_match.group(1)
            # Handle spans within the solution
            solution = clean_html_text(solution_text)
    
    # Extract discussion (content after three dots image and before related patterns)
    # Find content between threedots.jpg and the last set of pattern links
    discussion = ""
    
    # Find all content after the first threedots
    dots_pattern = r'<IMG SRC="[^"]*threedots\.jpg"[^>]*>'
    dots_matches = list(re.finditer(dots_pattern, content, re.IGNORECASE))
    
    if dots_matches:
        # Get content after first dots
        first_dots_end = dots_matches[0].end()
        # Find the last dots or the links section
        if len(dots_matches) > 1:
            last_dots_start = dots_matches[-1].start()
            discussion_section = content[first_dots_end:last_dots_start]
        else:
            # Find the end - look for the last pattern links or copyright
            copyright_match = re.search(r'<div align="center">\s*<h4><I>A Pattern Language</i>', content, re.IGNORECASE)
            if copyright_match:
                discussion_section = content[first_dots_end:copyright_match.start()]
            else:
                discussion_section = content[first_dots_end:]
        
        # Extract text - try different approaches
        discussion_parts = []
        
        # Method 1: Find h6 blocks (may not have closing tag, so find until next major tag)
        h6_start = discussion_section.find('<h6>')
        if h6_start >= 0:
            # Extract everything after <h6> up to the end or next major section
            h6_content = discussion_section[h6_start + 4:]  # Skip <h6>
            # Look for closing tag or end
            h6_end = h6_content.find('</h6>')
            if h6_end < 0:
                # No closing tag, use everything
                h6_text = h6_content
            else:
                h6_text = h6_content[:h6_end]
            
            # Now extract paragraphs from h6_text
            para_pattern = r'<P[^>]*>(.*?)</P>'
            for para_match in re.finditer(para_pattern, h6_text, re.DOTALL | re.IGNORECASE):
                text = clean_html_text(para_match.group(1))
                if text and not text.startswith('A Pattern Language') and len(text) > 10:
                    # Skip pattern reference lines at the end
                    if not re.search(r'\(\d+\)', text[-30:]):
                        discussion_parts.append(text)
            
            # Also get paragraphs not wrapped in <P> tags
            # Split by <P> tags first
            parts = re.split(r'<P[^>]*>.*?</P>', h6_text, flags=re.DOTALL | re.IGNORECASE)
            for part in parts:
                text = clean_html_text(part)
                if text and len(text) > 20 and not text.startswith('A Pattern Language'):
                    # Check if not already captured
                    if not any(text in existing or existing in text for existing in discussion_parts):
                        discussion_parts.append(text)
        
        # Method 2: Find all span class=h6class content
        text_pattern = r'<span class=h6class>(.*?)</span>'
        for match in re.finditer(text_pattern, discussion_section, re.DOTALL | re.IGNORECASE):
            text = clean_html_text(match.group(1))
            if text and not text.startswith('A Pattern Language') and len(text) > 10:
                # Check if not already captured
                if not any(text in part or part in text for part in discussion_parts):
                    discussion_parts.append(text)
        
        # Method 3: Extract plain paragraphs NOT inside h6 tags (for patterns like apl59)
        # Remove h6 blocks entirely first
        discussion_without_h6 = discussion_section
        if h6_start >= 0:
            # Remove everything from the first <h6> onwards
            discussion_without_h6 = discussion_section[:h6_start]
        
        # Now extract all <P> paragraphs
        para_pattern = r'<P[^>]*>(.*?)</P>'
        for match in re.finditer(para_pattern, discussion_without_h6, re.DOTALL | re.IGNORECASE):
            text = clean_html_text(match.group(1))
            if text and len(text) > 10 and not text.startswith('A Pattern Language'):
                # Check if not already captured
                if not any(text in part or part in text for part in discussion_parts):
                    discussion_parts.append(text)
        
        # Method 4: Extract plain text not in tags (loose text between tags)
        # Remove all tags but keep text
        loose_text_section = discussion_without_h6
        # Remove all <P>...</P> blocks
        loose_text_section = re.sub(r'<P[^>]*>.*?</P>', '', loose_text_section, flags=re.DOTALL | re.IGNORECASE)
        # Remove all other tags
        loose_text_section = re.sub(r'<[^>]+>', '', loose_text_section)
        text = clean_html_text(loose_text_section)
        if text and len(text) > 20:
            # Split by newlines and filter
            for line in text.split('\n'):
                line = line.strip()
                if line and len(line) > 20 and not any(line in part or part in line for part in discussion_parts):
                    discussion_parts.append(line)
        
        # Join all parts
        if discussion_parts:
            discussion = '\n\n'.join(discussion_parts)
    
    # Extract related patterns from the markdown file (preserve existing)
    # We'll handle this in the calling function
    
    return {
        'number': pattern_num,
        'title': pattern_title,
        'problem': problem,
        'solution': solution,
        'discussion': discussion
    }


def read_existing_related_patterns(md_path: str) -> str:
    """Read existing related patterns from markdown file."""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the Related Patterns section
        if '## Related Patterns' in content:
            related_section = content.split('## Related Patterns')[1]
            return '## Related Patterns' + related_section
        return ""
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
        return ""


def create_markdown_content(pattern_data: Dict[str, str], related_patterns: str) -> str:
    """Create complete markdown content from pattern data."""
    md_lines = []
    
    # Title
    md_lines.append(f"# {pattern_data['number']} - {pattern_data['title'].upper()}")
    md_lines.append("")
    
    # Problem section
    if pattern_data['problem']:
        md_lines.append("## Problem")
        md_lines.append("")
        md_lines.append(pattern_data['problem'])
        md_lines.append("")
    
    # Solution section (part of problem in Alexander's format)
    if pattern_data['solution']:
        md_lines.append(pattern_data['solution'])
        md_lines.append("")
    
    # Discussion section
    if pattern_data['discussion']:
        md_lines.append("## Discussion")
        md_lines.append("")
        md_lines.append(pattern_data['discussion'])
        md_lines.append("")
    
    # Related patterns (preserve existing)
    if related_patterns:
        md_lines.append(related_patterns)
    
    return '\n'.join(md_lines)


def complete_pattern(pattern_num: int, apl_dir: str, markdown_dir: str, dry_run: bool = False) -> bool:
    """Complete a single pattern markdown file from its HTML source."""
    # Format pattern number with leading zeros (always 3 digits)
    pattern_str = f"{pattern_num:03d}"
    
    # Find HTML file
    html_path = os.path.join(apl_dir, f"apl{pattern_num}.htm")
    if not os.path.exists(html_path):
        print(f"HTML file not found: {html_path}")
        return False
    
    # Find markdown file
    md_path = os.path.join(markdown_dir, f"apl{pattern_str}.md")
    if not os.path.exists(md_path):
        print(f"Markdown file not found: {md_path}")
        return False
    
    # Extract pattern data from HTML
    print(f"Processing pattern {pattern_num}: {html_path}")
    pattern_data = extract_pattern_from_html(html_path)
    
    if not pattern_data:
        print(f"Failed to extract pattern data from {html_path}")
        return False
    
    # Read existing related patterns
    related_patterns = read_existing_related_patterns(md_path)
    
    # Create complete markdown content
    markdown_content = create_markdown_content(pattern_data, related_patterns)
    
    if dry_run:
        print(f"Would write to {md_path}:")
        print(markdown_content[:500])
        print("...")
        return True
    
    # Write markdown file
    try:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✓ Updated {md_path}")
        return True
    except Exception as e:
        print(f"Error writing {md_path}: {e}")
        return False


def main():
    """Main function to complete all incomplete markdown patterns."""
    # Get repository root
    repo_root = Path(__file__).parent
    apl_dir = repo_root / "apl"
    markdown_dir = repo_root / "markdown" / "apl"
    
    # Find all incomplete patterns (those without Problem or Discussion sections)
    incomplete_patterns = []
    
    for md_file in sorted(markdown_dir.glob("apl*.md")):
        # Skip non-pattern files
        if not re.match(r'apl\d+\.md', md_file.name):
            continue
        
        # Read file and check if it has Problem or Discussion sections
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "## Problem" not in content and "## Discussion" not in content:
                # Extract pattern number
                match = re.match(r'apl(\d+)\.md', md_file.name)
                if match:
                    pattern_num = int(match.group(1))
                    incomplete_patterns.append(pattern_num)
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
    
    print(f"Found {len(incomplete_patterns)} incomplete patterns to process")
    print(f"APL directory: {apl_dir}")
    print(f"Markdown directory: {markdown_dir}")
    print()
    
    # Process each pattern
    success_count = 0
    fail_count = 0
    
    for pattern_num in incomplete_patterns:
        try:
            if complete_pattern(pattern_num, str(apl_dir), str(markdown_dir)):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"Error processing pattern {pattern_num}: {e}")
            fail_count += 1
    
    print(f"\nCompleted: {success_count} patterns")
    print(f"Failed: {fail_count} patterns")


if __name__ == "__main__":
    main()
