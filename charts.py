import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.title('Bar chart')
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.title('Pie chart')
    plt.show()


if __name__ == '__main__':
    labels = range(10)
    values = range(10)
    generate_bar_chart(labels, values)

    generate_pie_chart(labels, values)
