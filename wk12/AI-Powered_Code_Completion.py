"""
Task 1: AI-Powered Code Completion
Tool: Use a code completion tool like GitHub Copilot or Tabnine.
Task:
Write a Python function to sort a list of dictionaries by a specific key.
Compare the AI-suggested code with your manual implementation.
Document which version is more efficient and why.
Deliverable: Code snippets + 200-word analysis.
"""

# AI-Suggested Code (Example using GitHub Copilot)
def sort_dicts_by_key_ai(dicts, key):
    return sorted(dicts, key=lambda x: x[key])
# Manual Implementation
def sort_dicts_by_key_manual(dicts, key):
    for i in range(len(dicts)):
        for j in range(0, len(dicts)-i-1):
            if dicts[j][key] > dicts[j+1][key]:
                dicts[j], dicts[j+1] = dicts[j+1], dicts[j]
    return dicts
# Example usage
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_ai = sort_dicts_by_key_ai(data, 'age')   
sorted_manual = sort_dicts_by_key_manual(data.copy(), 'age')    
print("AI-Sorted:", sorted_ai)
print("Manual-Sorted:", sorted_manual)

# example 2 usage
countries = [{'country': 'USA', 'population': 331}, {'country': 'India', 'population': 1380}, {'country': 'China', 'population': 1441}, {'country': 'Brazil', 'population': 213}, {'country': 'Nigeria', 'population': 206}, {'country': 'Russia', 'population': 146}, {'country': 'Japan', 'population': 126}, {'country': 'Germany', 'population': 83}, {'country': 'France', 'population': 67}, {'country': 'UK', 'population': 66}, {'country': 'Italy', 'population': 60}, {'country': 'Canada', 'population': 38}, {'country': 'Australia', 'population': 25}, {'country': 'Spain', 'population': 47}, {'country': 'Mexico', 'population': 128}, {'country': 'Indonesia', 'population': 273}, {'country': 'Pakistan', 'population': 220}, {'country': 'Bangladesh', 'population': 164}, {'country': 'Philippines', 'population': 109}, {'country': 'Vietnam', 'population': 97}, {'country': 'Turkey', 'population': 84}, {'country': 'Iran', 'population': 83}, {'country': 'Thailand', 'population': 70}, {'country': 'Egypt', 'population': 102}, {'country': 'South Africa', 'population': 60}, {'country': 'Colombia', 'population': 51}, {'country': 'Argentina', 'population': 45}, {'country': 'Ukraine', 'population': 41}, {'country': 'Poland', 'population': 38}, {'country': 'Iraq', 'population': 40}, {'country': 'Canada', 'population': 38}, {'country': 'Morocco', 'population': 37}, {'country': 'Saudi Arabia', 'population': 35}, {'country': 'Uzbekistan', 'population': 34}, {'country': 'Peru', 'population': 33}, {'country': 'Angola', 'population': 33}, {'country': 'Malaysia', 'population': 32}, {'country': 'Ghana', 'population': 31}, {'country': 'Yemen', 'population': 30}, {'country': 'Nepal', 'population': 29}, {'country': 'Venezuela', 'population': 28}, {'country': 'Madagascar', 'population': 27}, {'country': 'Cameroon', 'population': 26}, {'country': 'Côte d\'Ivoire', 'population': 26}, {'country': 'North Korea', 'population': 25}, {'country': 'Australia', 'population': 25}, {'country': 'Niger', 'population': 24}, {'country': 'Sri Lanka', 'population': 21}, {'country': 'Burkina Faso', 'population': 21}, {'country': 'Mali', 'population': 20}, {'country': 'Romania', 'population': 19}, {'country': 'Malawi', 'population': 19}, {'country': 'Chile', 'population': 19}, {'country': 'Kazakhstan', 'population': 19}, {'country': 'Zambia', 'population': 18}, {'country': 'Guatemala', 'population': 18}, {'country': 'Ecuador', 'population': 17}, {'country': 'Syria', 'population': 17}, {'country': 'Netherlands', 'population': 17}, {'country': 'Senegal', 'population': 17}, {'country': 'Cambodia', 'population': 16}, {'country': 'Chad', 'population': 16}, {'country': 'Somalia', 'population': 16}, {'country': 'Zimbabwe', 'population': 15}, {'country': 'Guinea', 'population': 13}, {'country': 'Rwanda', 'population': 13}, {'country': 'Benin', 'population': 12}, {'country': 'Burundi', 'population': 12}, {'country': 'Tunisia', 'population': 12}, {'country': 'Bolivia', 'population': 11}, {'country': 'Belgium', 'population': 11}, {'country': 'Haiti', 'population': 11}, {'country': 'Cuba', 'population': 11}, {'country': 'South Sudan', 'population': 11}, {'country': 'Dominican Republic', 'population': 10}, {'country': 'Czech Republic', 'population': 10}, {'country': 'Greece', 'population': 10}, {'country': 'Jordan', 'population': 10}, {'country': 'Portugal', 'population': 10}, {'country': 'Azerbaijan', 'population': 10}, {'country': 'Sweden', 'population': 10}, {'country': 'Honduras', 'population': 10}, {'country': 'United Arab Emirates', 'population': 9}, {'country': 'Hungary', 'population': 9}, {'country': 'Tajikistan', 'population': 9}, {'country': 'Belarus', 'population': 9}, {'country': 'Austria', 'population': 9}, {'country': 'Papua New Guinea', 'population': 9}, {'country': 'Serbia', 'population': 8}]
sorted_countries_ai = sort_dicts_by_key_ai(countries, 'population')
sorted_countries_manual = sort_dicts_by_key_manual(countries.copy(), 'population')
print("AI-Sorted Countries by Population:", sorted_countries_ai)
print("Manual-Sorted Countries by Population:", sorted_countries_manual)

"""
Analysis:
Both the AI-suggested code and the manual implementation successfully sort a list of dictionaries by a specified key. However, they differ significantly in terms of efficiency and readability.

The AI-suggested code utilizes Python's built-in sorted() function, which is highly optimized for performance. This function employs Timsort, an efficient sorting algorithm with a time complexity of O(n log n) in the average and worst cases. The lambda function serves as a key extractor, allowing for concise and readable code.

In contrast, the manual implementation employs a nested loop to insert each dictionary into a new list in sorted order. This approach has a time complexity of O(n^2) in the worst case, as each insertion may require traversing the entire sorted list. Consequently, the AI-generated solution is significantly more efficient, both in terms of execution time and code clarity.

In conclusion, while both implementations achieve the same outcome, the AI-suggested code is superior due to its efficiency and simplicity, demonstrating the potential of AI tools in enhancing programming productivity.

"""