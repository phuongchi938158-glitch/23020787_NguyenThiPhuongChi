# LACTF_misc-EBE Write-up
LACTF_misc-EBE 

author task: burturt

I was trying to send a flag to my friend over UDP, one character at a time, but it got corrupted! I think someone else was messing around with me and sent extra bytes, though it seems like they actually abided by RFC 3514 for once. Can you get the flag?

A pcap file is attached to the task. In which only UDP protocols.

![image](https://user-images.githubusercontent.com/99678071/218249900-1a67486f-1c2b-4437-90b0-ac17fff7780b.png)

If you look at the session you can see this 

![image](https://user-images.githubusercontent.com/99678071/218249612-1709a7dc-c61d-4f2a-9cf5-bb19f0570868.png)

There is only 1 session in this traffic, so this information will not help us, it is clear that random characters + our flag. How to separate the flag? We know that the format of the flag is "lactf{..}" . Let's look at the hex value of the first one found {

![image](https://user-images.githubusercontent.com/99678071/218249750-eace3576-c045-4845-a412-d7f14a1ba057.png)

Looking at the other hex values, we see that they differ by 64 01 and e4 c0 

![image](https://user-images.githubusercontent.com/99678071/218249799-4921896b-382b-4713-ad57-8502024348eb.png)
![image](https://user-images.githubusercontent.com/99678071/218249819-1c33fb41-9280-4b11-8cd4-9444910c1abf.png)

Having collected all protocols having 64 c1 through the filter, we will get our flag: 
lactf{3V1L_817_3xf1l7R4710N_4_7H3_W1N_51D43c8000034d0c}
