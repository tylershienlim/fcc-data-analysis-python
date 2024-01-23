import numpy as np

def calculate(list):
    #List must contain nine numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #Change list into numpy array
    a = np.array(list)

    #Calculate flattened
    flat = []
    flat.append(np.mean(a))
    flat.append(np.var(a))
    flat.append(np.std(a))
    flat.append(max(list))
    flat.append(min(list))
    flat.append(sum(list))

    #Change numpy array into matrix
    matrix = a.reshape(3, 3)

    #Calculate for each row in matrix
    axis2 = [[],[],[],[],[],[]]

    for row in matrix:
        axis2[0].append(np.mean(row))
        axis2[1].append(np.var(row))
        axis2[2].append(np.std(row))
        axis2[3].append(np.max(row))
        axis2[4].append(np.min(row))
        axis2[5].append(sum(row))

    #Calculate for each column in matrix
    b = matrix.T
    axis1 = [[],[],[],[],[],[]]

    for row in b:
        axis1[0].append(np.mean(row))
        axis1[2].append(np.std(row))
        axis1[1].append(np.var(row))
        axis1[3].append(np.max(row))
        axis1[4].append(np.min(row))
        axis1[5].append(sum(row))

    calculations = {
        'mean':[],
        'variance':[],
        'standard deviation':[],
        'max':[],
        'min':[],
        'sum':[],
    }

    #Add to dictionary
    calculations['mean'] += [axis1[0]]
    calculations['mean'] += [axis2[0]]
    calculations['mean'].append(flat[0])

    calculations['variance'] += [axis1[1]]
    calculations['variance'] += [axis2[1]]
    calculations['variance'].append(flat[1])

    calculations['standard deviation'] += [axis1[2]]
    calculations['standard deviation'] += [axis2[2]]
    calculations['standard deviation'].append(flat[2])

    calculations['max'] += [axis1[3]]
    calculations['max'] += [axis2[3]]
    calculations['max'].append(flat[3])

    calculations['min'] += [axis1[4]]
    calculations['min'] += [axis2[4]]
    calculations['min'].append(flat[4])

    calculations['sum'] += [axis1[5]]
    calculations['sum'] += [axis2[5]]
    calculations['sum'].append(flat[5])

    return calculations