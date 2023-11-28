import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

st.title("Computer Network")


st.write("###")
st.write("###")
st.write("###")
# List of video URLs
video_urls = {
    "Importance of Computer Network":"https://www.youtube.com/watch?v=392cS7ae_bg&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=1&pp=iAQB",
    "Network Basic and Internet Hierarchy":"https://www.youtube.com/watch?v=HtPMB0DEGi4&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=2&pp=iAQB",
    "Network Topology":"https://www.youtube.com/watch?v=SKNdxLHebyg&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=3&pp=iAQB",
    "OSI Layer":"https://www.youtube.com/watch?v=ORLTYhYfWmQ&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=4&pp=iAQB",
    "Physical Link and Data Link Layer":"https://www.youtube.com/watch?v=JwDPsiz8k4g&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=5&pp=iAQB",
    "Network and Transport Layer":"https://www.youtube.com/watch?v=14trY1Fw01g&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=6&pp=iAQB",
    "Session, Presentation and Application Layer":"https://www.youtube.com/watch?v=i31BK2RrZ1g&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=7&pp=iAQB",
    "OSI Model vs TCP/IP Protocol Suite":"https://www.youtube.com/watch?v=ZYMRGBrNlQw&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=8&pp=iAQB",
    "TCP/IP Protocol Suite":"https://www.youtube.com/watch?v=g0VyUnrRLM8&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=9&pp=iAQB",
    "Addressing":"https://www.youtube.com/watch?v=c5eF7MFcx8g&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=10&pp=iAQB",
    "Basic of Modulation, Analog Signal, Digital Signal":"https://www.youtube.com/watch?v=x5EGHx_oZGo&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=11&pp=iAQB",
    "Over View Of Data and Signal":"https://www.youtube.com/watch?v=NvSI6Y-53Ow&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=12&pp=iAQB",
    "Error Detection and Error Correction":"https://www.youtube.com/watch?v=zh0Mogb81TU&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=13&pp=iAQB",
    "Wireless LAN Architecture":"https://www.youtube.com/watch?v=1KqjzTIgdYs&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=14&pp=iAQB",
    "MAC Layer of Wireless LAN":"https://www.youtube.com/watch?v=undySae_oSI&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=15&pp=iAQB",
    "Frame Format and Addressing mechanism":"https://www.youtube.com/watch?v=jpPOLggGyiM&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=16&pp=iAQB",
    "HSP and ESP":"https://www.youtube.com/watch?v=RPS-KUcaFEU&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=17&pp=iAQB",
    "Bluetooth Architecture":"https://www.youtube.com/watch?v=yIFtDBbCrpI&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=18&pp=iAQB",
    "Bluetooth Layering":"https://www.youtube.com/watch?v=XnnQ2852RI0&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=19&pp=iAQB",
    "IP Adress Basic":"https://www.youtube.com/watch?v=W2uBQnrbmh4&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=20&pp=iAQB",
    "Classful Address, Subnetting and Supernetting":"https://www.youtube.com/watch?v=XObGrrU5FQY&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=21&pp=iAQB",
    "Classless Addressing and NAT":"https://www.youtube.com/watch?v=rINSqA6N6D4&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=22&pp=iAQB",
    "ICMP":"https://www.youtube.com/watch?v=qoYaNMY1j2I&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=23&pp=iAQB",
    "what is the need of IP Address":"https://www.youtube.com/watch?v=voFG3jcvZZo&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=24&pp=iAQB",
    "IPv4 Datagram Fromat and Fragmentation":"https://www.youtube.com/watch?v=sAbfMq760O8&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=25&pp=iAQB",
    "IPv6 Datagram Format and Header Format":"https://www.youtube.com/watch?v=A8MbGwMWerc&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=26&pp=iAQB",
    "IPv4 VS IPv6 and Transition from IPv4 to IPv6":"https://www.youtube.com/watch?v=VbCQg0mP_yA&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=27&pp=iAQB",
    "Wifi":"https://www.youtube.com/watch?v=3fi5qeAOX2U&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=28&pp=iAQB",
    "6Low PAN":"https://www.youtube.com/watch?v=qJqT_VkW_cE&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=29&pp=iAQB",
    "Zigbee":"https://www.youtube.com/watch?v=VsYS1iCPbr4&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=30&pp=iAQB",
    "Packet Switched Network - Datagram":"https://www.youtube.com/watch?v=g4btdGjvCSY&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=31&pp=iAQB",
    "Packet Switched Network - Virtual Circuit":"https://www.youtube.com/watch?v=spMONA-3E30&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=32&pp=iAQB",
    "RIP Protocol":"https://www.youtube.com/watch?v=ibcVXvioaQo&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=33&pp=iAQB",
    "OSPF Protocol":"https://www.youtube.com/watch?v=0eWCdgPHuZg&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=34&pp=iAQB",
    "Global Internet":"https://www.youtube.com/watch?v=S6cE6Or8Iao&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=35&pp=iAQB",
    "Border Gateway Protocol - 1":"https://www.youtube.com/watch?v=lWIKNLzEXig&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=36&pp=iAQB",
    "Border Gateway Protocol - 2":"https://www.youtube.com/watch?v=lWIKNLzEXig&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=37&pp=iAQB",
    "Multicast Routing":"https://www.youtube.com/watch?v=TDLJ9vSFHhI&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=38&pp=iAQB",
    "RPF,RPB and RPM":"https://www.youtube.com/watch?v=bG3fgl_vsMc&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=39&pp=iAQB",
    "DM and SM - Multicast Routing":"https://www.youtube.com/watch?v=SDZ2pzKlHK8&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=40&pp=iAQB",
    "Process to Process Delivery and Port Number":"https://www.youtube.com/watch?v=CE7vB963ciQ&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=41&pp=iAQB",
    "TCP VS UDP":"https://www.youtube.com/watch?v=0R0NrNYiicU&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=42&pp=iAQB",
    "UDP":"https://www.youtube.com/watch?v=eKySjjLZKF0&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=43&pp=iAQB",
    "TCP":"https://www.youtube.com/watch?v=v_lDqJLiRfM&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=44&pp=iAQB",
    "TCP - Buffer, Segment and Segment Format":"https://www.youtube.com/watch?v=ZxPuzNDG2fo&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=45&pp=iAQB",
    "TCP - Connection Establishment - 1":"https://www.youtube.com/watch?v=hFLr33j7OJc&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=46&pp=iAQB",
    "TCP - Connection Establishment - 2":"https://www.youtube.com/watch?v=pSYxE3drqLQ&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=47&pp=iAQB",
    "TCP State Transition Diagram":"https://www.youtube.com/watch?v=gWdYaAjEkC4&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=48&pp=iAQB",
    "TCP Flow Control":"https://www.youtube.com/watch?v=DttfUa0rJX0&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=49&pp=iAQB",
    "TCP Error Control Technique - 1":"https://www.youtube.com/watch?v=JtByhgIKNKE&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=50&pp=iAQB",
    "TCP Error Control Technique - 2":"https://www.youtube.com/watch?v=JtByhgIKNKE&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=51&pp=iAQB",
    "TCP Congestion Control":"https://www.youtube.com/watch?v=h5HjdwkiurE&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=52&pp=iAQB",
    "TCP Congestion Avoidance":"https://www.youtube.com/watch?v=CZMAkWKPIBw&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=53&pp=iAQB",
    "Quality Of Service":"https://www.youtube.com/watch?v=xLUob4zwCy4&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=54&pp=iAQB",
    "Techniques to improve Quality of Service":"https://www.youtube.com/watch?v=uLJ_Tk0lo9w&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=55&pp=iAQB",
    "Application Requirements":"https://www.youtube.com/watch?v=8f9rFRBeVc8&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=56&pp=iAQB",
    "Email Architecture":"https://www.youtube.com/watch?v=DEl2P6NYcOY&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=57&pp=iAQB",
    "MIME and Email Format":"https://www.youtube.com/watch?v=DEl2P6NYcOY&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=57&pp=iAQB",
    "SMTP, POP3, IMAP - 1":"https://www.youtube.com/watch?v=aWrfOmVgBNY&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=59&pp=iAQB",
    "SMTP, POP3, IMAP - 2":"https://www.youtube.com/watch?v=aWrfOmVgBNY&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=60&pp=iAQB",
    "Domain Name Service - 1":"https://www.youtube.com/watch?v=EB-WVw6rfzg&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=61&pp=iAQB",
    "Domain Name Service - 2":"https://www.youtube.com/watch?v=K0FDYbYa8tA&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=62&pp=iAQB",
    "Domain Name Service - 3":"https://www.youtube.com/watch?v=4GJWwokH_-s&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=63&pp=iAQB",
    "Domain Name Service - 4":"https://www.youtube.com/watch?v=0akBY_QUnCg&list=PLbxBGRRnuvJf8xjhzcb9NbfcjFqkE_MMN&index=64&pp=iAQB"
    # Add more video URLs as needed
}

links = list(video_urls.keys())

tab1, tab2 = st.tabs(["VIdeos", "Notes"])



with tab1:
    c1,c2 = st.columns([7,3])

    title = "Computer Networks"
    # Sidebar to display video list
    with c2:
        selected_video_index = option_menu(title, links,default_index=0)

    with c1:
        st.markdown('### **'+selected_video_index+'**')
        st.video(video_urls[selected_video_index])


    js = '''
    <script>
        var body = window.parent.document.querySelector(".menu");
        console.log(body);
        body.scrollTop = 0;
    </script>
    '''

    st.components.v1.html(js)

with tab2:
    st.markdown("""
## Unit - 1:

[Important Notes](https://drive.google.com/file/d/13C71SwFUA1MFK8SMxUKbUr1yCyGHMps5/view?usp=sharing) 
                
## Unit - 2:

[Important Notes](https://drive.google.com/file/d/1dvOriUSdBxI8OYXBezmjgiDBIOflEsNl/view?usp=drive_link)
                
## Unit - 3:
                
[Important Notes](https://drive.google.com/file/d/1xea7t_xTrmRxorY3gAnxxK3B9UA8UDDH/view?usp=drive_link)
                

## Unit - 4:
                
[Important Notes](https://drive.google.com/file/d/1y_n_h7Zx6uYWAmRaNFr8knEorGtnjcgA/view?usp=drive_link)
            

## Unit - 5:
                
[Important Notes](https://drive.google.com/file/d/1cwM26W2nM8h78Io2EzNGY63RQFTfZJa9/view?usp=drive_link)
""")