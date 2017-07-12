class Network(object):
    def __init__(self, input, output, hidden = []):
        self.input_nodes = input
        self.output_nodes = output
        self.hidden_nodes = hidden
    def add_hidden_layer(self, neurons_count):
        self.hidden_nodes += [neurons_count]


    