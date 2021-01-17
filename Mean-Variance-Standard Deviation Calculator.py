import numpy as np

def calculate(list):
    mean = []
    variance = []
    StandardDeviation = []
    maximum = []
    minimum = []
    total = []

    a = np.array(list)
    try:
        a = np.reshape(a, (3, 3))
    except:
        raise ValueError("List must contain nine numbers.")

    mean.append(np.mean(a, axis=0).tolist())
    mean.append(np.mean(a, axis=1).tolist())
    mean.append(np.mean(a).tolist())

    variance.append(np.var(a, axis=0).tolist())
    variance.append(np.var(a, axis=1).tolist())
    variance.append(np.var(a).tolist())

    StandardDeviation.append(np.std(a, axis=0).tolist())
    StandardDeviation.append(np.std(a, axis=1).tolist())
    StandardDeviation.append(np.std(a).tolist())

    maximum.append(np.amax(a, axis=0).tolist())
    maximum.append(np.amax(a, axis=1).tolist())
    maximum.append(np.amax(a).tolist())

    minimum.append(np.amin(a, axis=0).tolist())
    minimum.append(np.amin(a, axis=1).tolist())
    minimum.append(np.amin(a).tolist())

    total.append(np.sum(a, axis=0).tolist())
    total.append(np.sum(a, axis=1).tolist())
    total.append(np.sum(a).tolist())

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': StandardDeviation,
        'max': maximum,
        'min': minimum,
        'sum': total
    }

    return calculations



