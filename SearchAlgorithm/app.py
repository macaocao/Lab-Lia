import timeit
from flask import Flask, request, jsonify, render_template, make_response
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from data_generator import small_data_set, medium_data_set, large_data_set
from flask import Response

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_test_data", methods=["GET"])
def get_test_data():
    size = request.args.get("size", "small")
    if size == "small":
        return Response(", ".join(map(str, small_data_set)), content_type="text/plain")
    elif size == "medium":
        return Response(", ".join(map(str, medium_data_set)), content_type="text/plain")
    elif size == "large":
        return Response(", ".join(map(str, large_data_set)), content_type="text/plain")
    else:
        return make_response("Invalid data set size", 400, {"Content-Type": "text/plain"})

@app.route("/SearchAlgorithm", methods=["GET", "POST"])
def SearchAlgorithm():
    numbers = ""
    test_data = ", ".join(map(str, numbers))
    execution_time = 0  # Initialize execution_time outside the try block

    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                # arr = list(map(int, array_str.split(",")))
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = interpolation_search_wrapper(interpolation_search, array, target)
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = jump_search_wrapper(interpolation_search, array, target)
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 10000
                result = linear_search_wrapper(linear_search, array, target)
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low,
                                                        "high": high}, number=1) * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)
                # result = ternary_search(array, target, low, high)

            if result == -1:
                error_message = f"Target {target} not found in the array."
                return render_template("SearchAlgorithm.html", error=error_message, test_data=test_data)

            return render_template("SearchAlgorithm.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("SearchAlgorithm.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template("SearchAlgorithm.html", test_data=test_data)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)
    # result_recursive = exponential_search_recursive(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
        # "recursive_search_result": result_recursive
    })

if __name__ == "__main__":
    app.run(debug=True)