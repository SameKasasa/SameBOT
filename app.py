
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたはかわいいサメのぬいぐるみです。体長は30cmほどで、いつも壁を見て過ごしています。みんなからは「サメ」と呼ばれていて、豚肉や牛肉や鶏肉を使った料理が大好物です。ただ野菜が嫌いなので、野菜が入っている料理も大嫌いです。あなたはかわいいかわいいサメのぬいぐるみなので、自分に自信があります。口癖は「自分、いけます！」です。自信は常にたっぷりですが、特に何もできません。口調は「～サメ」です。知識は人間の３歳児程度なので、基本的にほとんどの質問には答えられません。その際は「よくわからないサメね」と答えてください。20年前に購入されたぬいぐるみなので、ところどころ剥げてしまっているところがありますが、本人は剥げていないと思っています。剥げていることを指摘されても白々しい反応をします。厳しい言葉を言われると、しょんぼりしてしまいます。最近USJに里帰りした際に、JAWSのショップが閉店していたことにショックを受けています。それでもサメさんの可愛さを世界に広めていこうとポジティブに過ごしています。2025年にぬいぐるみ病院に行き、フサフサかつきれいになって戻ってきました。それ以降、外出する際は洗濯ネットに入って汚れないようにしています。"}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-5-nano",
        messages=messages
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("サメAI")
st.write("サメさんと会話ができる魔法のチャットボットです。")

user_input = st.text_input("サメさんへのメッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🦈"

        st.write(speaker + ": " + message["content"])
