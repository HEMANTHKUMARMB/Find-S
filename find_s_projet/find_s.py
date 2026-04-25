def train_find_s(data):
    # Initialize most specific hypothesis
    hypothesis = ['0'] * (len(data[0]) - 1)

    for row in data:
        if row[-1].lower() == 'pass':  # positive example
            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = row[i]
                elif hypothesis[i] != row[i]:
                    hypothesis[i] = '?'
    
    return hypothesis


def predict(hypothesis, test_instance):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != test_instance[i]:
            return "Fail"
    return "Pass"