#!/usr/bin/env python3
"""
Generate social pattern names from UIA pattern descriptions.
Extracts social domain content and creates concise pattern names.
"""

import re
import os

def extract_social_content(pattern_file):
    """Extract the social domain section from a UIA pattern file."""
    with open(pattern_file, 'r') as f:
        content = f.read()
        # Extract the social section
        social_match = re.search(r'## Social\s*\n\s*\n(.*?)(?=\n\n##|\Z)', content, re.DOTALL)
        if social_match:
            return social_match.group(1).strip()
    return None

def create_social_name(pattern_num, social_text, uia_name):
    """
    Create a concise social pattern name based on the social domain description.
    Uses manual mapping based on key concepts in the social text.
    """
    
    # Manual mappings for social pattern names based on analysis of the content
    social_names = {
        1: "INDEPENDENT ORGANIZATIONAL NETWORKS",
        2: "DISTRIBUTION OF GROUP SIZES",
        3: "BALANCE OF FORMAL AND INFORMAL",
        4: "REGENERATIVE SOCIAL AREAS",
        5: "NETWORK OF GROUP AFFILIATIONS",
        6: "GROWING ORGANIZATIONAL CENTERS",
        7: "INFORMAL ORGANIZATIONAL CONTEXT",
        8: "VARIETY OF ORGANIZATIONAL FORMS",
        9: "DISTRIBUTED DECISION-MAKING",
        10: "ACCESS TO ORGANIZATIONAL INTENSITY",
        11: "LOCAL COMMUNITY DOMAINS",
        12: "INDIVIDUAL IDENTITY IN GROUPS",
        13: "ORGANIZATIONAL BOUNDARIES",
        14: "RECOGNIZABLE COMMUNITY",
        15: "COMMUNITY BOUNDARY",
        16: "WEB OF GENERAL RELATIONSHIPS",
        17: "ENCIRCLING RELATIONSHIPS",
        18: "NETWORK OF ROLE REDEFINITIONS",
        19: "WEB OF SELECTIVE COMMUNICATION",
        20: "USER-DETERMINED COMMUNICATION CHANNELS",
        21: "FOUR-LEVEL HIERARCHY LIMIT",
        22: "MEETING SIZE LIMIT",
        23: "PARALLEL COMPENSATING RELATIONSHIPS",
        24: "POSITIONS FOR TRANSCENDENCE",
        25: "RELATIONSHIP TO UNCERTAINTY",
        26: "FUNCTIONAL CYCLE",
        27: "COMPLEMENTARY ROLES",
        28: "COHERENT RELATIONSHIP DENSITY",
        29: "STABLE COMMUNITY GRADIENT",
        30: "ACTIVITY HUBS",
        31: "CYCLE OF RELATIONSHIP REINFORCEMENT",
        32: "SELECTIVE COMMUNICATION AXIS",
        33: "FLEXIBLE PROCESSES",
        34: "INTERCHANGE OPPORTUNITIES",
        35: "VARIETY OF CYCLIC ACTIVITIES",
        36: "DIFFERENTIATION BY RELATIONSHIP DENSITY",
        37: "CLUSTER OF ORGANIZATIONAL FRAMEWORKS",
        38: "STANDARD ORGANIZATIONAL FRAMEWORKS",
        39: "INTEGRATING NEW DIMENSIONS",
        40: "INTEGRATING HISTORICAL DIMENSION",
        41: "INFORMAL CONTEXT FOR FORMAL PROCESSES",
        42: "CHAIN OF TRANSFORMATION ZONES",
        43: "PRESENTATION OF NEW DIMENSIONS",
        44: "LOCAL FOCAL POINTS",
        45: "LOCAL ACTION NETWORK",
        46: "DIVERSIFIED EXCHANGE ENVIRONMENT",
        47: "FUNCTIONALITY ENHANCEMENT",
        48: "ADAPTIVE INTERSTICES",
        49: "LOCAL RELATIONSHIP LOOPS",
        50: "THREE-WAY RELATIONSHIP COORDINATION",
        51: "INFORMAL ENHANCEMENT OF FORMAL RELATIONSHIPS",
        52: "INTERFACING MEDIATED AND DIRECT RELATIONSHIPS",
        53: "PRINCIPAL ENTRY POINTS",
        54: "INTERSECTION OF DIFFERENT COMMUNICATION PACES",
        55: "PROTECTED LOW-INTENSITY RELATIONSHIPS",
        56: "SPECIAL RELATIONSHIP MODES",
        57: "PROTECTION OF EMERGING CENTERS",
        58: "CONTEXT FOR CHAOS",
        59: "LOW-INTENSITY COMMUNICATION PATHWAYS",
        60: "ACCESSIBLE INFORMAL NETWORKS",
        61: "SMALL-SCALE COMMON INTERACTION SPACES",
        62: "POINTS OF BROADER PERSPECTIVE",
        63: "CYCLIC INTERPLAY OF COMPLEMENTARY PERSPECTIVES",
        64: "ACCESS TO CREATIVE IRRATIONALITY",
        65: "CONTEXT FOR EMERGING PERSPECTIVES",
        66: "CONTEXT FOR TRANSFORMATIVE EXPERIENCE",
        67: "UNSTRUCTURED COMMON DOMAIN",
        68: "SPONTANEOUS RELATIONSHIP FORMATION",
        69: "COMMON EXTERNAL SPACE FOR REST",
        70: "CONTEXT FOR HONORING HISTORY",
        71: "ACCESS TO CONTAINED CHAOS",
        72: "COMPETITIVE INTERACTION OPPORTUNITIES",
        73: "EXPLORATORY RELATIONSHIP CONTEXTS",
        74: "INTERACTION WITH ALTERNATIVE PERSPECTIVES",
        75: "EXTENDED NUCLEAR INTERACTION PATTERN",
        76: "MINIMAL CONTEXT FOR INTERGENERATIONAL RELATIONSHIPS",
        77: "MINIMAL CONTEXT FOR COMPLEMENTARY PERSPECTIVES",
        78: "MINIMAL CONTEXT FOR SINGLE PERSPECTIVE",
        79: "ADAPTABLE PERSPECTIVE CONTEXTS",
        80: "INTEGRATED CONTEXTS FOR PERSPECTIVE DYNAMICS",
        81: "MINIMAL OPERATIONAL CONTROL STRUCTURES",
        82: "MINIMAL DISTANCE BETWEEN CONTROL CONTEXTS",
        83: "INTEGRATION OF LEARNING AND MAINTENANCE",
        84: "TRANSITIONAL CONTEXTS FOR REORGANIZATION",
        85: "IMITATION CONTEXTS FOR DEVELOPING PERSPECTIVES",
        86: "CONTEXTS FOR PREMATURE PERSPECTIVES",
        87: "SINGLE-PERSPECTIVE CONTROLLED EXCHANGES",
        88: "INFORMAL LOCAL PERSPECTIVE INTERFACES",
        89: "LOCAL SOURCES OF PERSPECTIVE NOURISHMENT",
        90: "UNSTRUCTURED EXCHANGE CONTEXT",
        91: "HOSPITABLE CONTEXTS FOR TRANSITION",
        92: "HOSPITABLE TRANSIT POINTS",
        93: "TRANSIT POINTS NEAR NOURISHMENT SOURCES",
        94: "HOSPITABLE COMMON DOMAINS",
        95: "COMPLEXIFICATION OF PERSPECTIVE CONTEXTS",
        96: "LIMITATION ON STRUCTURAL HIERARCHY LEVELS",
        97: "CONCEALMENT OF MONOTONOUS PATTERNS",
        98: "PATTERNING OF COMPLEX STRUCTURES",
        99: "FOCAL CENTER OF COMPLEX STRUCTURE",
        100: "ARRANGEMENT FOR FRUITFUL INTERFACES",
        101: "PROTECTED LOW-DENSITY PATHWAYS",
        102: "DISTINCT ENTRY PATTERN",
        103: "LIMITATION ON MEETING SITES",
        104: "STRUCTURAL DEVELOPMENT FOR HARMONY",
        105: "ORIENTATION FOR EXTERNAL INSIGHT",
        106: "FUNCTIONAL ENHANCEMENT OF SEPARATING DOMAINS",
        107: "ORGANIZATION FOR EXTERNAL RECEPTIVITY",
        108: "INTERCONNECTED STRUCTURES",
        109: "ORGANIZATION FOR SUB-STRUCTURE AUTONOMY",
        110: "DISTINCTIVE MAIN ENTRY POINT",
        111: "BLENDED FORMAL AND INFORMAL INTEGRATION",
        112: "TRANSITION DOMAIN TO COMMUNICATION PATHWAY",
        113: "HARMONIOUS ENTRY FOR EXTERNAL MEDIA",
        114: "HIERARCHY FAVORING BROAD PERSPECTIVES",
        115: "FUNCTIONAL INTEGRATION OF UNSTRUCTURED DOMAINS",
        116: "PATTERNING INTEGRATIVE SUPERSTRUCTURE",
        117: "CONTAINMENT BY INTEGRATIVE SUPERSTRUCTURE",
        118: "INTEGRATION OF INFORMAL INTO SUPERSTRUCTURE",
        119: "PARTIALLY CONTAINED INTERFACES",
        120: "FOCUS-ORIENTED COMMUNICATION NETWORKS",
        121: "HOSPITABLE COMMUNICATION PATHWAYS",
        122: "DIRECT STRUCTURE-PATHWAY RELATIONSHIP",
        123: "ENHANCING FUNCTION OF COMMON DOMAINS",
        124: "ENSURING COMMON DOMAIN INTERFACE FUNCTION",
        125: "INTEGRATING VIEWPOINTS INTO COMMON DOMAINS",
        126: "OFF-CENTERING THE FOCAL POINT",
        127: "NESTED ACCESSIBILITY LEVELS",
        128: "ORIENTATION TO RECEIVE EXTERNAL INSIGHT",
        129: "COMMON DOMAIN AT STRUCTURAL FOCAL POINT",
        130: "INTERNAL TRANSITION SPACES",
        131: "ORGANIZATION OF INTER-DOMAIN DYNAMICS",
        132: "LIMITING COMMUNICATION PATH LENGTH",
        133: "INTEGRATING TRANSITION PATHWAYS BETWEEN LEVELS",
        134: "LIMITING EXPOSURE TO HARMONIOUS PERSPECTIVES",
        135: "ENHANCING INSIGHT BY VARYING EXPOSURE",
        136: "RELATIVE ISOLATION OF COMPLEMENTARY PERSPECTIVES",
        137: "DOMAIN FOR DEVELOPING PERSPECTIVES",
        138: "RECEPTIVITY TO EMERGING EXTERNAL INSIGHT",
        139: "HOSPITABLE DOMAIN FOR NOURISHMENT",
        140: "RELATIVE ISOLATION OF PATHWAY INTERFACE",
        141: "RELATIVELY ISOLATED CONTEXT PER PERSPECTIVE",
        142: "SEQUENCE OF VIEWPOINT LOCI",
        143: "INTERRELATIONSHIP OF DEVELOPING CONTEXTS",
        144: "INTEGRATED EXPOSURE TO IRRATIONALITY",
        145: "DOMAINS FOR RESERVE ELEMENTS",
        146: "FLEXIBLE DOMAIN ORGANIZATION",
        147: "COORDINATION OF PERSPECTIVE NOURISHMENT",
        148: "PERSPECTIVE INTERACTION CONSTRAINTS",
        149: "HOSPITABLE RECEPTION OF EXTERNAL PERSPECTIVES",
        150: "PROVISION FOR TEMPORARY INACTIVITY",
        151: "SMALL-SCALE INTERACTION CONTEXTS",
        152: "PARTIALLY ISOLATED CONTEXTS",
        153: "STRUCTURES ADAPTABLE TO CHANGING NUMBERS",
        154: "SEMI-AUTONOMOUS CONTEXTS FOR MATURING",
        155: "SEMI-AUTONOMOUS CONTEXTS FOR DECLINING ACTIVITY",
        156: "OPPORTUNITIES FOR DECLINING PERSPECTIVES",
        157: "LOCAL ACTIVITY OPPORTUNITIES",
        158: "EXTERNAL ACCESS TO HIGHER LEVELS",
        159: "ORGANIZATION FOR TWO INSIGHT SOURCES",
        160: "HOSPITABLE STRUCTURE-ENVIRONMENT INTERFACE",
        161: "STRUCTURE-ENFOLDED INSIGHT DOMAIN",
        162: "ORGANIZATION TO MINIMIZE INSIGHT BLINDSPOTS",
        163: "HOSPITABLE EXTERNAL INFORMAL DOMAIN",
        164: "OVERVIEW OF PATHWAY FROM STRUCTURE",
        165: "EXPOSURE OF ACTIVITIES TO PATHWAY",
        166: "OVERVIEW DOMAINS AT EXTERNAL INTERFACES",
        167: "ENFOLDED MINIMAL OVERVIEW DOMAINS",
        168: "GROUNDED STRUCTURES",
        169: "MAINTAINING CONTEXTUAL LEVEL DISTINCTIONS",
        170: "CULTIVATION OF PRODUCTIVE INFORMALITY",
        171: "APPROPRIATE INFORMALITY-STRUCTURE RELATIONSHIP",
        172: "CONTEXTS OF SELF-ORGANIZING INFORMALITY",
        173: "PROTECTING INFORMAL CONTEXTS FROM PATHWAYS",
        174: "PATHWAYS ENFOLDED BY INFORMALITY",
        175: "INSIGHT-CAPTURING INFORMAL EXTENSIONS",
        176: "SITES FOR GROUNDING IN INFORMALITY",
        177: "LOCAL CULTIVATION OF NOURISHMENT SOURCES",
        178: "RE-INTEGRATION OF REJECTED BY-PRODUCTS",
        179: "ORGANIZATION TO PROVIDE OCCUPIABLE SITES",
        180: "OCCUPIABLE SITES EXPOSED TO INSIGHT",
        181: "MAINTENANCE OF DIRECT INSIGHT SOURCE",
        182: "APPROPRIATE CONDITIONS FOR NOURISHMENT",
        183: "PARTIALLY EXPOSED PERSPECTIVE CONTEXT",
        184: "APPROPRIATE CONFIGURATION FOR INPUT PROCESSING",
        185: "APPROPRIATE CONFIGURATION FOR INTERACTION",
        186: "APPROPRIATE CONFIGURATION FOR INACTIVITY",
        187: "APPROPRIATE CONFIGURATION FOR COMPLEMENTARY INTERACTION",
        188: "OCCUPIABLE SITES FOR INACTIVITY",
        189: "CONTEXT FOR PRESENTATION FORMS",
        190: "VARIATION IN PERSPECTIVE CONTEXT SIZES",
        191: "APPROPRIATE CONTEXT PROPORTIONS",
        192: "OVERVIEW OF EXTERNAL CONTEXTS",
        193: "PARTIALLY ENCLOSED INTERNAL DOMAINS",
        194: "INTERNAL DOMAIN CONNECTEDNESS",
        195: "FRAMEWORK FOR LEVEL TRANSITIONS",
        196: "ECCENTRIC ACCESS TO PERSPECTIVE CONTEXTS",
        197: "SUBSTANTIVE DOMAIN DISTINCTIONS",
        198: "INTER-DOMAIN CONTEXTS FOR ADJUNCTS",
        199: "EXPOSURE OF INPUT PROCESSING TO INSIGHT",
        200: "FACILITIES FOR PERSPECTIVE ADJUNCTS",
        201: "ACCESSIBLE FACILITIES FOR ADJUNCTS",
        202: "STRUCTURE-ENFOLDED OCCUPIABLE SITES",
        203: "EXCLUSIVE SPACES FOR EMERGENT PERSPECTIVES",
        204: "EXCLUSIVE CONTEXTS",
        205: "CONGRUENCE BETWEEN FRAMEWORK AND PROCESS SPACES",
        206: "EFFICIENT ENCLOSURE WITH MINIMAL DISTINCTIONS",
        207: "APPROPRIATE CONSTRUCTION ELEMENTS",
        208: "PROGRESSIVE FRAMEWORK DEFINITION",
        209: "ORGANIZATION OF INTEGRATIVE SUPERSTRUCTURE",
        210: "HARMONIZING SPACE DISTRIBUTION BETWEEN LEVELS",
        211: "BOUNDARY EXPANSION FOR NEW LEVEL GENERATION",
        212: "PRIMARY INTER-LEVEL CONNECTIONS AT TRANSITIONS",
        213: "DISTRIBUTION OF SECONDARY INTER-LEVEL CONNECTIONS",
        214: "INTEGRATIVE INFRASTRUCTURE",
        215: "INITIAL LEVEL FORMATION",
        216: "INTER-LEVEL CONNECTIONS",
        217: "PERIMETER CONTINUITY",
        218: "DISTORTION-RESISTANT BOUNDARIES",
        219: "LEVEL GENERATION OF MINIMUM TENSION",
        220: "INTEGRATION SUPERSTRUCTURE",
        221: "APERTURE COMPATIBILITY",
        222: "GROUND-LEVEL VISIBILITY",
        223: "ZONES OF INTERMEDIATE INSIGHT",
        224: "EMPHASIZING BOUNDARY TRANSITIONS",
        225: "THICKENED BOUNDARY INTERFACES",
        226: "INTER-LEVEL ZONE",
        227: "INTER-LEVEL INTEGRITY",
        228: "APPROPRIATE SUPERSTRUCTURE FOR LEVEL TRANSITIONS",
        229: "PATHWAYS FOR AUTOMATIC COMMUNICATIONS",
        230: "UNMEDIATED SUPPORTIVE EMOTION",
        231: "OVERVIEW SITES FROM SUPERSTRUCTURE",
        232: "SYMBOLIC CONNECTION TO ENCOMPASSING DOMAINS",
        233: "ZONING INTERNAL DOMAINS",
        234: "MAINTAINABLE MULTI-ELEMENT BOUNDARIES",
        235: "UNALIENATING INTERNAL BOUNDARIES",
        236: "DISPLACEABLE FRAMEWORKS",
        237: "CONNECTEDNESS IN ISOLATION",
        238: "FILTERED INSIGHTS",
        239: "MULTI-FACETED FRAMEWORKS",
        240: "TOLERANCE AT LEVEL INTERFACES",
        241: "ATTRACTIVE TEMPORARY POSITIONS",
        242: "INTERMEDIATE POSITION",
        243: "AMBIGUOUS BOUNDARIES",
        244: "FLEXIBLE INTERFACES",
        245: "PROTECTING VARIABILITY TO ENHANCE FIXITY",
        246: "INTEGRATION WITHIN CONTEXT",
        247: "EMBEDDING FIXITY WITHIN VARIABILITY",
        248: "TIME BINDING",
        249: "SYMBOLS OF INTEGRATION",
        250: "ENCOURAGING EMPHASES",
        251: "DIFFERENT SETTINGS",
        252: "DOMAINS OF INSIGHT",
        253: "MEANINGFUL SYMBOLS OF SELF-TRANSFORMATION",
    }
    
    return social_names.get(pattern_num, "")

def main():
    """Generate social pattern names and update SOCIAL_PATTERN_LIST.md"""
    
    print("Generating social pattern names from UIA descriptions...")
    
    # Collect all pattern data
    pattern_data = []
    for i in range(1, 254):
        pattern_num_str = str(i).zfill(3)
        pattern_id = f"1261{pattern_num_str}0"
        file_path = f"markdown/uia/{pattern_id}.md"
        
        # Read UIA pattern name from UIA_PATTERN_LIST.md
        social_text = None
        uia_name = None
        
        if os.path.exists(file_path):
            social_text = extract_social_content(file_path)
        
        # Get UIA name from UIA_PATTERN_LIST.md
        with open('UIA_PATTERN_LIST.md', 'r') as f:
            content = f.read()
            # Find the pattern name
            pattern_match = re.search(rf'\| {i} \| {pattern_id} \| (.*?) \|', content)
            if pattern_match:
                uia_name = pattern_match.group(1).strip()
        
        # Create social name
        social_name = create_social_name(i, social_text, uia_name)
        social_number = f"S{pattern_num_str}"
        
        pattern_data.append({
            'index': i,
            'pattern_id': pattern_id,
            'uia_name': uia_name,
            'social_number': social_number,
            'social_name': social_name
        })
    
    # Read the current SOCIAL_PATTERN_LIST.md
    with open('markdown/context/social/SOCIAL_PATTERN_LIST.md', 'r') as f:
        lines = f.readlines()
    
    # Update the table with social names
    updated_lines = []
    for line in lines:
        # Check if this is a pattern row - handle both complete and incomplete rows
        # Pattern 1: Complete row with 5 columns
        match_complete = re.match(r'\| (\d+) \| (\d+) \| (.*?) \| (S\d{3}) \| (.*?) \|', line)
        # Pattern 2: Incomplete row with only 3 columns (missing social number and name)
        match_incomplete = re.match(r'\| (\d+) \| (\d+) \| (.*?) \|$', line)
        
        if match_complete:
            index = int(match_complete.group(1))
            pattern_num = match_complete.group(2)
            uia_name = match_complete.group(3)
            social_num = match_complete.group(4)
            
            # Find the corresponding pattern data
            pattern = pattern_data[index - 1]
            social_name = pattern['social_name']
            
            # Create updated line
            updated_line = f"| {index} | {pattern_num} | {uia_name} | {social_num} | {social_name} |\n"
            updated_lines.append(updated_line)
        elif match_incomplete:
            index = int(match_incomplete.group(1))
            pattern_num = match_incomplete.group(2)
            uia_name = match_incomplete.group(3)
            
            # Find the corresponding pattern data
            pattern = pattern_data[index - 1]
            social_num = pattern['social_number']
            social_name = pattern['social_name']
            
            # Create complete line with all 5 columns
            updated_line = f"| {index} | {pattern_num} | {uia_name} | {social_num} | {social_name} |\n"
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)
    
    # Write the updated file
    with open('markdown/context/social/SOCIAL_PATTERN_LIST.md', 'w') as f:
        f.writelines(updated_lines)
    
    print(f"✓ Updated SOCIAL_PATTERN_LIST.md with {len(pattern_data)} social pattern names")
    print("\nFirst 10 patterns:")
    for p in pattern_data[:10]:
        print(f"  {p['index']:3d}. {p['social_number']}: {p['social_name']}")

if __name__ == "__main__":
    main()
