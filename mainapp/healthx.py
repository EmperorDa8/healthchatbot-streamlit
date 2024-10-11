import streamlit as st
import streamlit.components.v1 as components

# Streamlit UI Components
with st.container():
    st.image("img/labbot.jpg", width=200)
    st.title("Healthx AI Chatbot")
    st.write("This app is an assistant to medical practitioners to augument them .")

# HTML code to embed the Coze Web SDK chat client
    html_code = """
<!doctype html>
<html lang="en">
<head>
    <style>
        /* Customize the position of the chatbot */
        #chatbot-container {
            position: absolute;
            right: 10px;
            bottom: 20px;
            width: 400px;
            height: 550px;
        }
    </style>
</head>
<body>
    <div id="chatbot-container"></div>

    <script src="https://sf-cdn.coze.com/obj/unpkg-va/flow-platform/chat-app-sdk/0.1.0-beta.5/libs/oversea/index.js"></script>
    <script>
        new CozeWebSDK.WebChatClient({
            config: {
                bot_id: '7420144951037870085',  // 
            },
            componentProps: {
                title: 'Healthx Assistant',
            },
            el: document.getElementById('chatbot-container')  // Attach the chatbot to this div
        });
    </script>
</body>
</html>
"""

# Render the HTML code inside the Streamlit app
    components.html(html_code, height=600)





