from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np

def home(request):
    P0 = request.POST.get('p0') 
    D0 = request.POST.get('d0') 
    T0 = request.POST.get('t0') 
    N0 = request.POST.get('n0') 
    # P0 = 30
    # D0 = 10
    # T0 = 40
    # N0 = 10

    if P0 is not None:
        P0 = int(P0)
    else:
        # Handle the case where 'p0' is not present in the POST data
        # You might want to set a default value or show an error message
        P0 = 30

    if D0 is not None:
        D0 = int(D0)
    else:
        # Handle the case where 'd0' is not present in the POST data
        D0 = 20

    if T0 is not None:
        T0 = int(T0)
    else:
        # Handle the case where 't0' is not present in the POST data
        T0 = 15

    if N0 is not None:
        N0 = int(N0)
    else:
        # Handle the case where 'n0' is not present in the POST data
        N0 = 10


    t = np.linspace(0, 10, 100)
    N_t = (P0 - D0) / T0 * t + N0

    # plt.plot(range(10))
    plt.figure(figsize=(10, 6))
    plt.plot(t, N_t, label='Number of Packets (N(t))', color='blue')
    plt.title('Model of Network Traffic Over Time')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Number of Network Packets')
    plt.legend()
    plt.grid(True)

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data':uri, 'p0_data':P0, 'd0_data': D0, 't0_data': T0, 'n0_data': N0})

# Create your views here.
