from django.http import HttpResponse
from data import myContent


def home_page(request):
    entries = ""  # to store all
    for item in myContent:
        row = f"""
            <tr> 
                <td>{item["name"]}</td>
                <td>{item["age"]}</td>
                <td>{item["height"]}</td>
                <td>{item["bloodgroup"]}</td>
            </tr>
        """
        entries += row + "\n"

    html_code = f"""
        <h1>Hello world</h1>
        <table> 
            <thead> 
                <tr>
                    <th>name</th>
                    <th>age</th>
                    <th>height</th>
                    <th>bloodGroup</th>
                </tr>
            </thead>

            <tbody> 
                {entries}
            </tbody>

        </table>
    """
    print(html_code)
    return HttpResponse(html_code)
