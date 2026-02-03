#!/usr/bin/env python3
"""
Restructure APL pattern markdown files to match the required format:
1. Title: # Pattern: [number] - [NAME]
2. ## Narrower: Introductory paragraph linking to preceding patterns (from broader patterns)
3. ## Problem: Bold summary + details/background/manifestations
4. ## Solution: Bold solution + detailed explanation  
5. ## Broader: Paragraph linking to smaller completing patterns (from narrower patterns)

The classic Alexander pattern format has:
- Introductory paragraph that references broader patterns (context)
- Problem statement (bold)
- Solution statement after "Therefore:" (bold)
- Detailed discussion of problem and solution
- Concluding paragraph that references narrower patterns (implementation)
"""

import re
import os
from pathlib import Path
from typing import Optional, Dict

def extract_pattern_content(filepath: Path) -> Dict[str, str]:
    """Extract content from existing pattern markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title (e.g., "# 1 - INDEPENDENT REGIONS")
    title_match = re.search(r'^#\s+(\d+)\s*-\s*(.+)$', content, re.MULTILINE)
    if not title_match:
        print(f"Warning: No title found in {filepath}")
        return None
    
    pattern_num = title_match.group(1)
    pattern_name = title_match.group(2).strip()
    
    # Extract Problem section (everything between ## Problem and next ##)
    problem_match = re.search(r'##\s*Problem\s*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    problem_section = problem_match.group(1).strip() if problem_match else ""
    
    # Extract Discussion section
    discussion_match = re.search(r'##\s*Discussion\s*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    discussion_section = discussion_match.group(1).strip() if discussion_match else ""
    
    # Extract Related Patterns section
    related_match = re.search(r'##\s*Related Patterns\s*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    related_section = related_match.group(1).strip() if related_match else ""
    
    return {
        'number': pattern_num,
        'name': pattern_name,
        'problem_section': problem_section,
        'discussion_section': discussion_section,
        'related_section': related_section
    }

def split_problem_and_solution(problem_section: str) -> tuple[str, str]:
    """
    Split the problem section into problem summary and solution.
    In the current format:
    - First paragraph: problem summary (should be bold in output)
    - Rest: solution statement (should be bold in output)
    """
    paragraphs = problem_section.split('\n\n')
    
    if len(paragraphs) >= 2:
        problem_summary = paragraphs[0].strip()
        solution_statement = '\n\n'.join(paragraphs[1:]).strip()
    else:
        problem_summary = problem_section.strip()
        solution_statement = ""
    
    return problem_summary, solution_statement

def extract_narrower_context(discussion: str) -> tuple[str, str]:
    """
    Extract the narrower context (introductory paragraph) from discussion.
    This is the opening paragraph that refers to broader/preceding patterns.
    Usually starts with ". . ." and contains references to larger patterns.
    """
    # Look for introductory paragraph that starts with ". . ."
    narrower_match = re.match(r'^\.\s*\.\s*\.\s*(.+?)(?=\n\n)', discussion, re.DOTALL)
    if narrower_match:
        narrower = narrower_match.group(1).strip()
        # Remove the narrower part from discussion
        remaining = discussion[narrower_match.end():].strip()
        return narrower, remaining
    
    # If no ". . .", check if first paragraph references patterns
    paragraphs = discussion.split('\n\n', 1)
    if len(paragraphs) > 1:
        first_para = paragraphs[0]
        # Check if it contains pattern references (uppercase with numbers)
        if re.search(r'[A-Z][A-Z\s]+\(\d+\)', first_para):
            return first_para.strip(), paragraphs[1].strip()
    
    return "", discussion

def extract_broader_context(discussion: str, related_patterns: str) -> tuple[str, str]:
    """
    Extract the broader context (concluding paragraph/sentence) from discussion.
    The broader context refers to narrower/following patterns for implementation.
    It often starts with ". . ." or imperative verbs like "Make", "Give", "Shape".
    """
    # First try to find ". . ." that's not at the very beginning
    # This marks transition to smaller patterns
    dots_pattern = r'(\.\s*\.\s*\.\s*.+?)(?:\s+A Pattern Language is published|\Z)'
    dots_match = re.search(dots_pattern, discussion, re.DOTALL)
    
    if dots_match:
        # Check if this looks like a broader context (has pattern refs)
        potential_broader = dots_match.group(1).strip()
        if re.search(r'[A-Z][A-Z\s]+\(\d+\)', potential_broader):
            # Extract from the position of ". . ." onward
            broader_start = dots_match.start()
            broader = potential_broader
            remaining = discussion[:broader_start].strip()
            return broader, remaining
    
    # Alternative: look for last sentence(s) with implementation language
    # Split by ". " to get sentences
    sentences = discussion.split('. ')
    
    # Look for the last few sentences that have pattern references
    broader_sentences = []
    for i in range(len(sentences) - 1, max(len(sentences) - 10, -1), -1):
        sent = sentences[i]
        if re.search(r'[A-Z][A-Z\s]+\(\d+\)', sent):
            broader_sentences.insert(0, sent)
            # Check if this sentence has implementation language
            if re.search(r'\b(make|give|shape|provide|arrange|build|place|use|create)\b', sent, re.IGNORECASE):
                # Found it - join these sentences
                broader = '. '.join(broader_sentences)
                if not broader.endswith('.'):
                    broader += '.'
                remaining = '. '.join(sentences[:i])
                if remaining and not remaining.endswith('.'):
                    remaining += '.'
                return broader.strip(), remaining.strip()
        else:
            # No more pattern refs, stop looking
            if broader_sentences:
                broader = '. '.join(broader_sentences)
                if not broader.endswith('.'):
                    broader += '.'
                remaining = '. '.join(sentences[:i+1])
                if remaining and not remaining.endswith('.'):
                    remaining += '.'
                return broader.strip(), remaining.strip()
            break
    
    # If still nothing found, try splitting paragraphs and taking the last with pattern refs
    paragraphs = discussion.split('\n\n')
    if len(paragraphs) > 1:
        last_para = paragraphs[-1]
        if re.search(r'[A-Z][A-Z\s]+\(\d+\)', last_para):
            # Check if it's relatively short (likely a conclusion)
            if len(last_para) < 500:
                return last_para.strip(), '\n\n'.join(paragraphs[:-1]).strip()
    
    # Default: create a generic broader context
    return "To complete this pattern, use the related patterns listed below to implement the necessary details.", discussion

def restructure_pattern(data: Dict[str, str]) -> str:
    """Create restructured markdown content with proper headers."""
    if not data:
        return ""
    
    # Split problem into summary and solution
    problem_summary, solution_statement = split_problem_and_solution(data['problem_section'])
    
    # Extract narrower (intro) and broader (conclusion) contexts
    narrower, remaining_discussion = extract_narrower_context(data['discussion_section'])
    broader, problem_discussion = extract_broader_context(remaining_discussion, data['related_section'])
    
    # Build the new markdown structure
    output = []
    
    # Title with "# Pattern:" header
    output.append(f"# Pattern: {data['number']} - {data['name']}")
    output.append("")
    
    # Narrower section - introductory paragraph linking to preceding/broader patterns
    output.append("## Narrower:")
    output.append("")
    if narrower:
        output.append(narrower)
    else:
        # Provide a default if no narrower context found
        output.append("This pattern helps to complete the larger patterns in which it is embedded.")
    output.append("")
    
    # Problem section - bold summary + all problem/solution discussion
    output.append("## Problem:")
    output.append("")
    # Problem summary in bold
    output.append(f"**{problem_summary}**")
    output.append("")
    # All the problem/solution discussion goes here
    if problem_discussion:
        output.append(problem_discussion)
        output.append("")
    
    # Solution section - bold solution statement
    output.append("## Solution:")
    output.append("")
    # Solution statement in bold
    if solution_statement:
        output.append(f"**{solution_statement}**")
        output.append("")
    
    # Broader section - concluding paragraph linking to smaller/narrower patterns
    output.append("## Broader:")
    output.append("")
    if broader:
        output.append(broader)
    else:
        output.append("Complete this pattern by using the smaller patterns that follow to build out the details.")
    output.append("")
    
    # Add related patterns reference if they exist
    if data['related_section']:
        output.append("---")
        output.append("")
        output.append("### Related Patterns")
        output.append("")
        output.append(data['related_section'])
        output.append("")
    
    return '\n'.join(output)

def process_all_patterns(input_dir: str = 'markdown/apl', output_dir: str = 'markdown/apl'):
    """Process all pattern files in the directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Find all pattern files (apl001.md through apl253.md)
    pattern_files = sorted(input_path.glob('apl*.md'))
    
    success_count = 0
    fail_count = 0
    
    for filepath in pattern_files:
        # Skip non-numbered pattern files
        if not re.match(r'apl\d+\.md', filepath.name):
            continue
        
        print(f"Processing {filepath.name}...")
        
        try:
            # Extract content
            data = extract_pattern_content(filepath)
            if not data:
                fail_count += 1
                continue
            
            # Restructure
            new_content = restructure_pattern(data)
            
            # Write output
            output_file = output_path / filepath.name
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            success_count += 1
            
        except Exception as e:
            print(f"Error processing {filepath.name}: {e}")
            fail_count += 1
    
    print(f"\nProcessing complete:")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")

def main():
    """Main entry point."""
    base_dir = Path(__file__).parent
    input_dir = base_dir / 'markdown' / 'apl'
    
    if not input_dir.exists():
        print(f"Error: Directory {input_dir} not found")
        return
    
    print(f"Restructuring patterns in {input_dir}...")
    process_all_patterns(str(input_dir))

if __name__ == '__main__':
    main()
