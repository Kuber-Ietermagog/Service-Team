from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, ListView
from django.template.loader import render_to_string, get_template
from clock_card.models import ClockEntry
from django.contrib.auth.models import Permission, User
from . import forms
from datetime import *
import geocoder
import time

# Create your views here.

class MyClockCardList(View):

    def get(self, request, *args, **kwargs):
        filter_name = self.request.user.username
        this_month = datetime.today().strftime("%Y-%m")
        pay_month = datetime.today().strftime("%m")
        pay_year = datetime.today().strftime("%Y")
        this_day = datetime.today().strftime("%d")
        if int(this_day) < 20:
            if pay_month == "01":
                display_filter = ClockEntry.objects.filter(name=self.request.user.username,
                    date__range=[(str(int(pay_year) - 1)+"-"+str(int(pay_month)+11)+"-20"), (this_month + str("-20"))])
            else:
                display_filter = ClockEntry.objects.filter(name=self.request.user.username,
                    date__range=[(pay_year+"-"+str(int(pay_month)-1)+"-20"), (this_month + str("-20"))])
        else:
            if pay_month != "12":
                display_filter = ClockEntry.objects.filter(name=self.request.user.username,
                    date__range=[(pay_year+"-"+str(int(pay_month))+"-20"), (pay_year + "-" + str(int(pay_month) + 1) + str("-20"))])
            else:
                display_filter = ClockEntry.objects.filter(name=self.request.user.username,
                    date__range=[(pay_year + "-"+str(int(pay_month))+"-20"), (str(int(pay_year) + 1)) + "-" + str(int(pay_month) - 11) + str("-20")])
        dpi = 0
        time_worked = []
        clocked_hours = []
        same_day = "Yes"
        for items in display_filter:
            if dpi < len(display_filter) - 1:
                t1 = datetime.strptime(str(display_filter[dpi].date).replace('+00:00', ''), "%Y-%m-%d %H:%M:%S")
                t2 = datetime.strptime(str(display_filter[dpi+1].date).replace('+00:00', ''), "%Y-%m-%d %H:%M:%S")
                c1 = display_filter[dpi].clock_io
                c2 = display_filter[dpi+1].clock_io
                if (t1.day != t2.day) and (c1 == "Out") and (c2 == "In"):
                    same_day = "No"
                if (t1.day == t2.day) and (c1 == "Out") and (c2 == "In"):
                    same_day = "Yes"
            time_worked.append([display_filter[dpi].hours_worked, same_day])
            dpi += 1
        dpi = 0
        time_clocked = timedelta(0, 0)
        for items in time_worked:
            if time_worked[dpi][0] != "":
                if len(time_worked[dpi][0]) > 8:
                    extra = time_worked[dpi][0].replace("s, ", "").replace(", ", "").split(" day")
                    h_m_s = extra[1].split(":")
                    d = extra[0]
                    time_clocked += timedelta(days=int(d), hours=int(h_m_s[0]), minutes=int(h_m_s[1]), seconds=int(h_m_s[2]))
                else:
                    h_m_s = time_worked[dpi][0].split(":")
                    time_clocked = time_clocked + timedelta(hours=int(h_m_s[0]), minutes=int(h_m_s[1]), seconds=int(h_m_s[2]))
            dpi += 1
        clock_in_hrs = str(time_clocked).replace("s, ", "").replace(", ", "").split(" day")
        if len(clock_in_hrs) == 1:
            time_clocked = str(time_clocked)
        else:
            m_s = clock_in_hrs[1].split(":")
            h = int(clock_in_hrs[0])*24 + int(m_s[0])
            time_clocked = str(h) + ":" + m_s[1] + ":" + m_s[2]
        return render(request, 'clock_card/clock.html', {'display_filter': display_filter, 'time_clocked': time_clocked})

class ClockEventCreateView(CreateView):
    fields = "__all__"
    model = ClockEntry

    def get_initial(self):
        initial = super(ClockEventCreateView, self).get_initial()
        initial.update({'name': self.request.user.username})
        return initial

    def post(self, request, *args, **kwargs):
        this_month = datetime.today().strftime("%Y-%m")
        pay_month = datetime.today().strftime("%m")
        pay_year = datetime.today().strftime("%Y")
        this_day = datetime.today().strftime("%d")
        # display_filter = ClockEntry.objects.filter(name=self.request.user.username, date__range=[datetime.today().strftime("%Y-%m") + "-" + str(int(this_day) - 7),
        #     datetime.today().strftime("%Y-%m") + "-" + str(int(this_day) + 7)])
        display_filter = ClockEntry.objects.filter(name=self.request.user.username)[:1]
        name = request.POST.get('name')
        date = request.POST.get('date')
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        if len(display_filter) == 0:
            clock = "In"
            work = request.POST.get('work_st')
        if len(display_filter) != 0:
            if display_filter[0].clock_io == "In":
                clock = "Out"
                work = display_filter[0].work_st
                map_settings = '&zoom=18.85&size=300x300&markers=color:red|label:P|'
            else:
                work = request.POST.get('work_st')
                clock = "In"
                if work != "Travel":
                    map_settings = '&zoom=18.85&size=300x300&markers=color:orange|label:P|'
                else:
                    map_settings = '&zoom=18.85&size=300x300&markers=color:green|label:P|'
        #gps = geocoder.mapquest([lat, lon], method='reverse', key='JupixZGTQMsr5qIjL2lZXu9VjPP5H7GT')
        gps = geocoder.google([lat, lon], method='reverse', key='AIzaSyCdo7IoKzzwVmrc0ljNkKvYy5GrXef4iog')
        address = gps.address
        city = gps.city
        state = gps.state
        country = gps.country
        save_clock = ClockEntry()
        api_url = 'https://maps.googleapis.com/maps/api/staticmap?center='
        lat_long =  lat + "," + lon
        #map_settings = '&zoom=15&size=300x300&markers=color:green|label:P|'
        api_key = '&key=AIzaSyCdo7IoKzzwVmrc0ljNkKvYy5GrXef4iog'
        save_clock.name = name
        save_clock.date = date
        save_clock.latitude = lat
        save_clock.longitude = lon
        save_clock.address = address
        #save_clock.city = city
        #save_clock.state = state
        #save_clock.country = country
        save_clock.work_st = work
        save_clock.clock_io = clock
        save_clock.map_url = api_url + lat_long + map_settings + lat_long + api_key
        if clock == "Out":
            tz_diff = timedelta(0, 7200)
            hrs_work = datetime.strptime(date, "%Y-%m-%d %H:%M:%S") - datetime.strptime(str(display_filter[0].date).replace('+00:00', ''), "%Y-%m-%d %H:%M:%S")
            save_clock.hours_worked = str(hrs_work - tz_diff)
        else:
            save_clock.hours_worked = ""
        save_clock.save()
        return redirect('clock_card:clock')
