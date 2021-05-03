from django.shortcuts import redirect, render
from django.http import HttpResponse

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "4e9b259ec7mshc5d134eafa4d64cp118433jsn59788bd7b64b",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.
def index(request):
    if request.method=='POST':
        selectedCountry = request.POST['selectedCountry']

        totalresults = int(response['results'])
        countriesList = []


        for x in range(0,totalresults):
            country = response['response'][x]['country']
            countriesList.append(country)

            if selectedCountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['new']
                if recovered == 'None':
                    recovered = 0
                death = int(total) - int(active) - int(recovered)


        context = {'countries':countriesList,
                    'new':new,
                    'active':active,
                    'critical':critical,
                    'recovered':recovered,
                    'total':total,
                    'death':death}

        return render(request, 'index.html', context)




    totalresults = int(response['results'])
    countriesList = []
    for x in range(0,totalresults):
        country = response['response'][x]['country']
        countriesList.append(country)
    return render(request, 'index.html',
            {'countries':countriesList})
