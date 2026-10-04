def calculate_metrics(data_list):
    total = sum(data_list)
    avg = total / len(data_list) if data_list else 0
    max_val = max(data_list) if data_list else 0
    return {
        "count": len(data_list),
        "total": total,
        "average": avg,
        "maximum": max_val
    }

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    metrics = calculate_metrics(sample_data)
    print("Metrics summary:", metrics)
