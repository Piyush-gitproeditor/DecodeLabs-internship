def calculate_score(cpu, gpu, primary_use, total_price):
    if primary_use == "Gaming":
        cpu_score = cpu["Gaming_Score_0_100"]
        gpu_score = gpu["Gaming_Score_0_100"]

    elif primary_use == "Programming":
        cpu_score = cpu["Programming_Score_0_100"]
        gpu_score = gpu["Programming_Score_0_100"]

    elif primary_use == "Video Editing":
        cpu_score = cpu["Editing_Score_0_100"]
        gpu_score = gpu["Editing_Score_0_100"]

    elif primary_use == "AI / ML":
        cpu_score = cpu["AI_Score_0_100"]
        gpu_score = gpu["AI_Score_0_100"]

    else:
        return 0

    performance_score = (cpu_score + gpu_score) / 2

    value_score = 100000 / total_price
    value_score = min(value_score, 100)

    final_score = (
        performance_score * 0.8
        + value_score * 0.2
    )

    return round(final_score, 2)


def generate_explanation(build, primary_use, budget, ram_required, storage_required_gb):
    explanation = []

    explanation.append(
        f"Recommended for {primary_use}."
    )

    explanation.append(
        f"Total price is ${build['Total_Price']:,.2f}, "
        f"which is within your ${budget:,.2f} budget."
    )

    explanation.append(
        f"Recommendation score: {build['Score']}/100."
    )

    explanation.append(
        f"The configuration satisfies your {ram_required} GB RAM requirement "
        f"and {storage_required_gb:g} GB storage requirement."
    )

    return explanation
