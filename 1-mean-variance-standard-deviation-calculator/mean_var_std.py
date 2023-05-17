import numpy as np

def array_stat(mat, computation, ax=None):
    result = computation(mat,axis=ax)
    # print(result.tolist())
    return result.tolist()

def array_stats(mat, computation):
    return [array_stat(mat, computation ,ax=0), array_stat(mat, computation ,ax=1), array_stat(mat, computation)]

def calculate(list):
    ops = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    try:
        matrice = np.array(list).reshape(3,3)
    except ValueError as ve:
        raise ValueError("List must contain nine numbers.")
    form = { 
      'mean': [],
      'variance': [],
      'standard deviation': [],
      'max': [],
      'min': [],
      'sum': []
    } 
    
#     for oid, op in enumerate(ops):
#         form.values()[oid] =  array_stats(matrice, op)
#         print(array_stats(matrice, op))
    stats= []
    for op in ops:    
        stats.append(array_stats(matrice, op))
    
    print(stats[0])
    
    form['mean'].extend(stats[0])
    form['variance'].extend(stats[1])
    form['standard deviation'].extend(stats[2])
    form['max'].extend(stats[3])
    form['min'].extend(stats[4])
    form['sum'].extend(stats[5])
    
    # trial = array_stats(matrice, np.sum)
    
    # print(list, matrice, means, variances, trial)
    # calculations = 0
    return form

print(calculate([0,1,2,3,4,5,6,7,8]))


