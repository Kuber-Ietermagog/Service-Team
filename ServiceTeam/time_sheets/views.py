from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate,login,logout
from accounts.models import UserProfileInfo
from clock_card.models import ClockEntry
from django.views.generic import ListView, View
from datetime import *

# Create your views here.

class TeamListView(View):

    def get(self, request, *args, **kwargs):
        team_members = UserProfileInfo.objects.all()
        this_month = datetime.today().strftime("%Y-%m")
        pay_month = datetime.today().strftime("%m")
        return render(request, 'time_sheets/team_list.html', {'team_members': team_members, 'this_month': this_month})

    def post(self, request, *args, **kwargs):
        member = request.POST['thisMember']
        this_month = datetime.today().strftime("%Y-%m")
        pay_month = datetime.today().strftime("%m")
        pay_year = datetime.today().strftime("%Y")
        empl_no = ""
        user_info = UserProfileInfo.objects.all()
        for items in user_info:
            if items.user.username == member:
                mate_name = items.user.first_name
                mate_surname = items.user.last_name
                department = items.department
                job_title = items.job_title
                empl_no = items.employee_no
        financial_month = (pay_year+"-"+str(int(pay_month)-1)+"-20") + " to " + (this_month + str("-20"))
        display_filter = ClockEntry.objects.filter(name=member, date__range=[(pay_year+"-"+str(int(pay_month)-1)+"-19"), (this_month + str("-21"))])
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
        return render(request, 'time_sheets/person_time.html', {'myClockCard': display_filter, 'time_clocked': time_clocked,
            'this_month': financial_month, 'mate_name': mate_name,
             'mate_surname': mate_surname, 'employee_no': empl_no,
             'job_title': job_title, 'department': department})
