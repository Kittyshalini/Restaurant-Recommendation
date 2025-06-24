import pickle

df = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(name):
    try:
        i = df[df['name'] == name].index[0]
    except IndexError:
        return []

    data = similarity[i]
    listed = list(enumerate(data))
    top_5 = sorted(listed, reverse=True, key=lambda x: x[1])[1:6]

    recommendations = [df.iloc[i[0]]['name'] for i in top_5]
    return recommendations