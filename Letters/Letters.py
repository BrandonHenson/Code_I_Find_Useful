import time
## mm/yyyy format
date = (time.strftime("%m/%d/%Y"))
customer =[
["Ambrosia","415 Lincoln Ave","Grease Trap"],
["Azteca","11811 Mukilteo Speedway","Grease Trap"],
["Bite of New York","10100 Mukilteo Speedway","Grease Trap"],
["Brooklyn Bros. Pizza","8326 Mukilteo Speedway","Grease Trap"],
["Charles At Smugglers","8340 53rd Ave W","Grease Trap"],
["Diamond Knot","621 Front St","Grease Trap"],
["Garlic Jim's","10924 Mukilteo Speedway","Grease Trap"],
["Grouchy Chef","4433 Russell Rd","Grease Trap"],
["Gyro Stop","11811 Mukilteo Speedway","Grease Trap"],
["H.P. Middle School","5000 Harbour Pointe Blvd","Grease Trap"],
["H.P. Retirement","10200 Harbour Place","Grease Trap"],
["Hanami","11811 Mukilteo Speedway","Grease Trap"],
["Henry's Donuts","10924 Mukilteo Speedway","Grease Trap"],
["John's Grill","649 5th St","Grease Trap"],
["Kamiak High School","10801 Harbour Pt Blvd N","Grease Trap"],
["King's Teriyaki","8229 44th Ave W","Grease Trap"],
["Kosta's","8306 Mukilteo Speedway","Grease Trap"],
["Lotus","10924 Mukilteo Speedway","Grease Trap"],
["Mukilteo Chocolate Co.","407 Lincoln Ave","Grease Trap"],
["Mukilteo Lodge","7928 Mukilteo Speedway","Grease Trap"],
["Mukilteo Thai","8410 Mukilteo Speedway","Grease Trap"],
["Patty's Egg Nest","8204 Mukilteo Speedway","Grease Trap"],
["Pizza Hut","11707 Mukilteo Speedway","Grease Trap"],
["Rainbow Wok & Teriyaki","8410 Mukilteo Speedway","Grease Trap"],
["Rosehill Community Center","304 Lincoln Ave","Grease Trap"],
["Sabor A Mexico","8410 Mukilteo Speedway","Grease Trap"],
["Shake 'n Go","9999 Harbour Place","Grease Trap"],
["Starbucks","10100 Mukilteo Speedway","Grease Trap"],
["Staybridge Suites","9600 Harbour Place","Grease Trap"],
["Sully's","403 Lincoln Ave","Grease Trap"],
["The Scotsman","11601 Harbour Pointe Blvd","Grease Trap"],
["The Sydney Bakery","613 5th St","Grease Trap"],
["Traxx","4329 Chennault Beach Rd","Grease Trap"],
["Weller's","8490 Mukilteo Speedway","Grease Trap"],
["Z's Burgers","8307 Mukilteo Speedway","Grease Trap"],
["A Burger Place","11601 Harbour Pt Blvd","Grease Interceptor"],
["Arnie's","714 2nd St","Grease Interceptor"],
["Café Soleil","9999 Harbour Place","Grease Interceptor"],
["Fra Amici","8004 Mukilteo Speedway","Grease Interceptor"],
["Hilton Garden Inn","8401 Paine Field Blvd","Grease Interceptor"],
["Ivar's","710 Front St","Grease Interceptor"],
["Kamiak High School","10801 Harbour Pt Blvd N","Grease Interceptor"],
["Kiss Of The Ocean","801 2nd St","Grease Interceptor"],
["Lombardo's Pizza","10809 Mukilteo Speedway","Grease Interceptor"],
["Mongolian Grill","11700 Mukilteo Speedway","Grease Interceptor"],
["Mukilteo Shell","10900 Mukilteo Speedway","Grease Interceptor"],
["Mukilteo's Spdwy Cafe","11707 Mukilteo Speedway","Grease Interceptor"],
["Sakuma","10924 Mukilteo Speedway","Grease Interceptor"],
["Subway","9999 Harbour Place","Grease Interceptor"],
["Taco Bell","8401 Mukilteo Speedway","Grease Interceptor"],
["Whidbey Island Coffee","204 Lincoln Ave","Grease Interceptor"],
["H.P. Auto Bath","11400 Mukilteo Speedway","Oil \ Water Seperator"],
["Karmichael Auto Salon","11400 'B' Mukilteo Speedway","Oil \ Water Seperator"],
["Les Schwab","11500 Mukilteo Speedway","Oil \ Water Seperator"],
["The Spot","8203 Mukilteo Speedway","Oil \ Water Seperator"],
["Mukilteo Shell","10900 Mukilteo Speedway","Oil \ Water Seperator"],
["Smart Auto Service","11338 Mukilteo Speedway","Oil \ Water Seperator"],
#["Washington Air National Guard","Paine Field","Oil \ Water Seperator"]
]
ind = 0
for i in customer:
    name = (customer[ind][0])
    address = (customer[ind][1])
    typeof = (customer[ind][2])
    ind = int(ind)+1
    fileread = open('LetterToOpenAndRead.txt','r')
    filename = str(name)+'.doc'
    fileobj = open(filename, 'w')
    fileobj.write(fileread.read().format(date,name,typeof,address))
    fileobj.close()

