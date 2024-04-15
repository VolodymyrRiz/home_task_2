from abc import ABC, abstractmethod


class Output(ABC):

    @abstractmethod
    def consol_output(self):
        pass

    @abstractmethod
    def table_output(self):
        pass


class ConsolOutput(Output):

    def consol_output(self):
        return "This is a console output."

    # table_output is not applicable for ConsolOutput, so it should not be abstract
    def table_output(self):
        # You can either raise a NotImplementedError or provide a default implementation
        raise NotImplementedError("table_output is not implemented for ConsolOutput")

class TableOutput(Output):

    # consol_output is not applicable for TableOutput, so it should not be abstract
    def consol_output(self):
        # You can either raise a NotImplementedError or provide a default implementation
        raise NotImplementedError("consol_output is not implemented for TableOutput")

    def table_output(self):
        return "This is another table output."

data = input("Enter the type of output (consol or table): ")


# Instantiate the classes
if data == "c": 
    consol_view = ConsolOutput()
    print(consol_view.consol_output())
if data == "t": 
    table_view = TableOutput()
    print(table_view.table_output())

# Call the methods

