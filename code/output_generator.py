def generate_output(
    claim_row,
    claim_result,
    image_result,
    history_row=None
):

    risk_flags = []

    if not image_result["valid_image"]:
        risk_flags.append(
            "blurry_image"
        )

    if history_row is not None:

        flags = str(
            history_row["history_flags"]
        )

        if flags != "none":

            for flag in flags.split(";"):
                risk_flags.append(flag)

    claim_issue = str(
        claim_result["claimed_issue"]
    ).lower()

    image_issue = str(
        image_result["issue_type"]
    ).lower()

    claim_part = str(
        claim_result["claimed_part"]
    ).lower()

    image_part = str(
        image_result["object_part"]
    ).lower()

    # --------------------
    # DAMAGE EQUIVALENCE
    # --------------------

    equivalent_damage = {

        "crack": [
            "crack",
            "shatter"
        ],

        "shatter": [
            "crack",
            "shatter"
        ],

        "broken": [
            "broken",
            "missing"
        ],

        "missing": [
            "broken",
            "missing"
        ]
    }

    # --------------------
    # STATUS LOGIC
    # --------------------

    if (
        image_issue == "unknown"
        or
        claim_issue == "unknown"
    ):

        claim_status = (
            "not_enough_information"
        )

    elif image_issue == "none":

        claim_status = (
            "contradicted"
        )

    else:

        damage_match = False

        if claim_issue == image_issue:
            damage_match = True

        elif (
            claim_issue
            in equivalent_damage
            and
            image_issue
            in equivalent_damage[
                claim_issue
            ]
        ):
            damage_match = True

        part_match = False

        if (
            claim_part != "unknown"
            and
            claim_part in image_part
        ):
            part_match = True

        if (
            damage_match
            and
            part_match
        ):
            claim_status = (
                "supported"
            )

        elif damage_match:

            claim_status = (
                "not_enough_information"
            )

        else:

            claim_status = (
                "contradicted"
            )

    if len(risk_flags) == 0:
        risk_flags_text = "none"
    else:
        risk_flags_text = ";".join(
            risk_flags
        )

    return {

        "user_id":
        claim_row["user_id"],

        "image_paths":
        claim_row["image_paths"],

        "user_claim":
        claim_row["user_claim"],

        "claim_object":
        claim_row["claim_object"],

        "evidence_standard_met":
        image_result.get(
            "evidence_standard_met",
            True
        ),

        "evidence_standard_met_reason":
        image_result.get(
            "evidence_reason",
            ""
        ),

        "risk_flags":
        risk_flags_text,

        "issue_type":
        image_result["issue_type"],

        "object_part":
        image_result["object_part"],

        "claim_status":
        claim_status,

        "claim_status_justification":
        f"Claim says {claim_issue} on {claim_part}. Image shows {image_issue} on {image_part}.",

        "supporting_image_ids":
        "img_1",

        "valid_image":
        image_result["valid_image"],

        "severity":
        image_result["severity"]
    }