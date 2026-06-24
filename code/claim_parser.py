def extract_claim(user_claim):

    text = str(user_claim).lower()

    found_issue = "unknown"
    found_part = "unknown"

    # --------------------
    # ISSUE DETECTION
    # --------------------

    if "shatter" in text:
        found_issue = "shatter"

    elif "dent" in text or "dented" in text:
        found_issue = "dent"

    elif "scratch" in text or "scratched" in text:
        found_issue = "scratch"

    elif "crack" in text or "cracked" in text:
        found_issue = "crack"

    elif "broken" in text or "broke" in text:
        found_issue = "broken"

    elif "missing" in text:
        found_issue = "missing"

    elif "torn" in text:
        found_issue = "torn"

    elif "crushed" in text:
        found_issue = "crushed"

    elif "water" in text or "wet" in text:
        found_issue = "water"

    elif "stain" in text or "stained" in text:
        found_issue = "stain"

    # --------------------
    # PART DETECTION
    # --------------------

    if "front bumper" in text:
        found_part = "front bumper"

    elif "rear bumper" in text:
        found_part = "rear bumper"

    elif "side mirror" in text or "mirror" in text:
        found_part = "side mirror"

    elif "headlight" in text:
        found_part = "headlight"

    elif "taillight" in text or "tail light" in text or "back light" in text:
        found_part = "taillight"

    elif "windshield" in text or "front glass" in text:
        found_part = "windshield"

    elif "hood" in text:
        found_part = "hood"

    elif "door" in text:
        found_part = "door"

    elif "trackpad" in text:
        found_part = "trackpad"

    elif "keyboard" in text or "keycaps" in text or "keys" in text:
        found_part = "keyboard"

    elif "hinge" in text:
        found_part = "hinge"

    elif "lid" in text:
        found_part = "lid"

    elif "screen" in text or "display" in text or "pantalla" in text:
        found_part = "screen"

    elif "body" in text:
        found_part = "body"

    elif "base" in text:
        found_part = "base"

    elif "port" in text:
        found_part = "port"

    elif "package corner" in text or "box corner" in text:
        found_part = "corner"

    elif "corner" in text:
        found_part = "corner"

    elif "label" in text:
        found_part = "label"

    elif "seal" in text:
        found_part = "seal"

    elif "contents" in text:
        found_part = "contents"

    elif "item" in text:
        found_part = "item"

    elif "box" in text or "package" in text or "parcel" in text:
        found_part = "box"

    return {
        "claimed_issue": found_issue,
        "claimed_part": found_part
    }