import numpy as np
import pandas as pd
import statistics

def calculate_statistics(stock_data):
    """
    Calculates statistical characteristics of the given data.

    Args:
        data (pandas.DataFrame): Stock data.

    Returns:
        dict: Dictionary containing statistical characteristics.
    """
    statistics_values = {
        'mean': np.mean(stock_data['Close']),
        'std_dev': np.std(stock_data['Close']),
        'min': np.min(stock_data['Close']),
        'max': np.max(stock_data['Close']),
        "range": max(stock_data['Close']) - min(stock_data['Close']),
        "median": statistics.median(stock_data['Close']),
        "variance": statistics.variance(stock_data['Close'])
    }
    return statistics_values