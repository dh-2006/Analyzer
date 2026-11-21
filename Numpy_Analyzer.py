import numpy as np


class DataAnalytics:

    def __init__(self):
        self.__array = None

    @classmethod
    def project_title(cls):
        return "NumPy Analyzer"

    @staticmethod
    def check_choice(choice):
        return choice.isdigit()

    # Private method for showing array info
    def __show_info(self):
        print("\n[Array Shape:", self.__array.shape, "| Dimension:", str(self.__array.ndim) + "D]")

    def get_number(self, message):
        while True:
            try:
                number = int(input(message))
                if number > 0:
                    return number
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Enter a valid number.")

    def get_values(self, count):
        while True:
            try:
                values = input(
                    "Enter " + str(count) +
                    " elements separated by space: "
                ).split()

                if len(values) != count:
                    print("Please enter exactly", count, "elements.")
                    continue

                values = [int(x) if x.lstrip('-').isdigit() else float(x) for x in values]
                return values

            except ValueError:
                print("Invalid input! Enter only numbers.")

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = self.get_number("Enter the number of elements: ")
            values = self.get_values(n)

            self.__array = np.array(values)

        elif choice == "2":
            rows = self.get_number("Enter the number of rows: ")
            cols = self.get_number("Enter the number of columns: ")

            count = rows * cols
            values = self.get_values(count)

            self.__array = np.array(values).reshape(rows, cols)

        elif choice == "3":
            depth = self.get_number("Enter the number of layers: ")
            rows = self.get_number("Enter the number of rows: ")
            cols = self.get_number("Enter the number of columns: ")

            count = depth * rows * cols
            values = self.get_values(count)

            self.__array = np.array(values).reshape(depth, rows, cols)

        else:
            print("Invalid choice!")
            return

        print("\nArray created successfully:")
        print(self.__array)
        self.__show_info()

        self.array_operations()

    def array_operations(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.indexing()

            elif choice == "2":
                self.slicing()

            elif choice == "3":
                break

            else:
                print("Invalid choice!")

    def indexing(self):
        print("\nOriginal Array:")
        print(self.__array)

        try:
            index = int(input("Enter index: "))
            print("Element at index:", self.__array.flat[index])

        except (ValueError, IndexError):
            print("Invalid index!")

    def slicing(self):
        print("\nOriginal Array:")
        print(self.__array)

        if self.__array.ndim == 1:
            try:
                row_range = input("Enter the range (start:end): ").split(":")
                r1, r2 = int(row_range[0]), int(row_range[1])

                print("\nSliced Array:")
                print(self.__array[r1:r2])

            except (ValueError, IndexError):
                print("Invalid range!")

        elif self.__array.ndim == 2:
            try:
                row_range = input(
                    "Enter the row range (start:end): "
                ).split(":")

                col_range = input(
                    "Enter the column range (start:end): "
                ).split(":")

                r1, r2 = int(row_range[0]), int(row_range[1])
                c1, c2 = int(col_range[0]), int(col_range[1])

                print("\nSliced Array:")
                print(self.__array[r1:r2, c1:c2])

            except (ValueError, IndexError):
                print("Invalid range!")

        else:
            try:
                layer = int(input("Enter layer index: "))
                row_range = input(
                    "Enter row range (start:end): "
                ).split(":")
                col_range = input(
                    "Enter column range (start:end): "
                ).split(":")

                r1, r2 = int(row_range[0]), int(row_range[1])
                c1, c2 = int(col_range[0]), int(col_range[1])

                print("\nSliced Array:")
                print(self.__array[layer, r1:r2, c1:c2])

            except (ValueError, IndexError):
                print("Invalid range!")

    def mathematical_operations(self):
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            print("\nEnter the same-size array elements (" + str(self.__array.size) + " elements):")
            values = self.get_values(self.__array.size)
            second_array = np.array(values).reshape(self.__array.shape)

            print("\nOriginal Array:")
            print(self.__array)

            print("\nSecond Array:")
            print(second_array)

            if choice == "1":
                result = self.__array + second_array
                name = "Addition"

            elif choice == "2":
                result = self.__array - second_array
                name = "Subtraction"

            elif choice == "3":
                result = self.__array * second_array
                name = "Multiplication"

            elif choice == "4":
                if np.any(second_array == 0):
                    print("Division by zero is not allowed.")
                    return

                result = self.__array / second_array
                name = "Division"

            print("\nResult of", name + ":")
            print(result)

        elif choice == "5":
            if self.__array.ndim != 1:
                print("Dot product requires a 1D array!")
                return

            values = self.get_values(self.__array.size)
            second_array = np.array(values)

            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Array:")
            print(second_array)
            print("\nDot Product:", np.dot(self.__array, second_array))

        elif choice == "6":
            if self.__array.ndim != 2:
                print("Matrix multiplication requires a 2D array!")
                return

            rows = self.get_number("Enter rows for second matrix: ")
            cols = self.get_number("Enter columns for second matrix: ")

            if rows != self.__array.shape[1]:
                print("Matrix dimensions are not compatible!")
                return

            values = self.get_values(rows * cols)
            second_array = np.array(values).reshape(rows, cols)

            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Matrix:")
            print(second_array)
            print("\nMatrix Multiplication:")
            print(np.matmul(self.__array, second_array))

        else:
            print("Invalid choice!")

    def combine_split(self):
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter the elements of another array to combine (" + str(self.__array.size) + " elements):")
            values = self.get_values(self.__array.size)
            second_array = np.array(values).reshape(self.__array.shape)

            print("\nOriginal Array:")
            print(self.__array)

            print("\nSecond Array:")
            print(second_array)

            if self.__array.ndim == 1:
                result = np.concatenate((self.__array, second_array))
                print("\nCombined Array:")
                print(result)

            else:
                result = np.vstack((self.__array, second_array))
                print("\nCombined Array (Vertical Stack):")
                print(result)

        elif choice == "2":
            print("\nOriginal Array:")
            print(self.__array)

            if self.__array.shape[0] >= 2:
                result = np.array_split(self.__array, 2, axis=0)
                print("\nSplit Array:")
                for part in result:
                    print(part)

            else:
                print("Array cannot be split into 2 parts.")

        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nOriginal Array:")
            print(self.__array)

            try:
                value = float(input("Enter value to search: "))
                result = np.where(self.__array == value)

                if len(result[0]) > 0:
                    print("Value found at index:", result)
                else:
                    print("Value not found.")

            except ValueError:
                print("Enter a valid number.")

        elif choice == "2":
            print("\n1. Ascending")
            print("2. Descending")
            order = input("Enter your choice: ")

            print("\nOriginal Array:")
            print(self.__array)

            if order == "1":
                print("\nSorted Array:")
                print(np.sort(self.__array))
                if self.__array.ndim > 1:
                    print("(Sorting applied row-wise.)")

            elif order == "2":
                print("\nSorted Array:")
                print(-np.sort(-self.__array))
                if self.__array.ndim > 1:
                    print("(Sorting applied row-wise.)")

            else:
                print("Invalid choice!")

        elif choice == "3":
            print("\nOriginal Array:")
            print(self.__array)

            try:
                limit = float(input("Enter filter value: "))
                print("Values greater than", limit, ":")
                print(self.__array[self.__array > limit])

            except ValueError:
                print("Enter a valid number.")

        else:
            print("Invalid choice!")

    def statistics(self):
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation")

        choice = input("Enter your choice: ")

        print("\nOriginal Array:")
        print(self.__array)

        if choice == "1":
            print("\nSum of Array:", np.sum(self.__array))

        elif choice == "2":
            print("\nMean of Array:", np.mean(self.__array))

        elif choice == "3":
            print("\nMedian of Array:", np.median(self.__array))

        elif choice == "4":
            print("\nStandard Deviation of Array:", np.std(self.__array))

        elif choice == "5":
            print("\nVariance of Array:", np.var(self.__array))

        elif choice == "6":
            print("\nMinimum of Array:", np.min(self.__array))

        elif choice == "7":
            print("\nMaximum of Array:", np.max(self.__array))

        elif choice == "8":
            try:
                p = float(input("Enter percentile (0 to 100): "))
                if 0 <= p <= 100:
                    print("\nPercentile of Array:", np.percentile(self.__array, p))
                else:
                    print("Percentile must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "9":
            values = self.get_values(self.__array.size)
            second_array = np.array(values).reshape(self.__array.shape)
            corr = np.corrcoef(self.__array.flatten(), second_array.flatten())[0, 1]
            print("\nCorrelation Coefficient:", corr)

        else:
            print("Invalid choice!")

    def run(self):
        print("Welcome to the " + self.project_title() + "!")
        print("=" * 50)

        while True:
            print("\nChoose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if not self.check_choice(choice):
                print("Invalid input! Enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                self.create_array()

            elif choice in [2, 3, 4, 5]:
                if self.__array is None:
                    print("Please create an array first (Option 1).")
                    continue

                if choice == 2:
                    self.mathematical_operations()

                elif choice == 3:
                    self.combine_split()

                elif choice == 4:
                    self.search_sort_filter()

                elif choice == 5:
                    self.statistics()

            elif choice == 6:
                print("\nThank you for using the " + self.project_title() + "!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please select from 1 to 6.")


obj = DataAnalytics()
obj.run()