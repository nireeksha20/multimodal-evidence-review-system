import pandas as pd

from claim_parser import extract_claim
from image_analyzer import analyze_image
from output_generator import generate_output

claims = pd.read_csv("../dataset/claims.csv")
history = pd.read_csv("../dataset/user_history.csv")

results = []

print("Claims:", len(claims))

for index, row in claims.iterrows():

    image_paths = row["image_paths"].split(";")

    best_result = None

    severity_score = {
        "unknown": 0,
        "none": 0,
        "low": 1,
        "medium": 2,
        "high": 3
    }

    for path in image_paths:

        full_path = "../dataset/" + path

        image_result = analyze_image(full_path)

        if best_result is None:
            best_result = image_result

        else:

            current_score = severity_score.get(
                image_result.get("severity", "unknown"),
                0
            )

            best_score = severity_score.get(
                best_result.get("severity", "unknown"),
                0
            )

            if current_score > best_score:
                best_result = image_result

    claim_result = extract_claim(
        row["user_claim"]
    )

    history_match = history[
        history["user_id"] == row["user_id"]
    ]

    history_row = None

    if len(history_match) > 0:
        history_row = history_match.iloc[0]

    output_row = generate_output(
        row,
        claim_result,
        best_result,
        history_row
    )

    results.append(output_row)

    print(
        f"{index+1}/{len(claims)} processed"
    )

output_df = pd.DataFrame(results)

output_df.to_csv(
    "../output.csv",
    index=False
)

print("\nDONE")
print("output.csv created")