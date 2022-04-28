// 서버에 GET, POST 요청을 보내기 위해 구현된 라이브러리 함수입니다
// 여러분들이 나중에 프로젝트 하실때도, 별도로 구현 안하고 이를 활용하시면 됩니다
import { fetchGET, fetchPOST } from "./dataFetching.js";

// SERVER의 주소입니다
const SERVER_HOST =
  "https://asia-northeast3-likelion-js-practice.cloudfunctions.net/api";

// 서버에 어떤 사람의 정보를 달라고 요청할지에 대한 변수입니다
const NAME = "김영권";

// 프로필 조희를 위한 함수 (name, mbti, github)
// async라는 키워드를 function 앞에 명시해야, 함수 내에서 await를 사용할 수 있습니다
async function getProfileData(name) {
  // 프로필 조회를 위한 서버의 EndPoint
  const path = "/member";

  // 서버에 GET요청을 보내서 응답을 받습니다
  // 이때 서버에서 응답이 넘어오는데는 시간이 소요되고,
  // Javascript의 비동기적 흐름 때문에 await를 사용하여 응답이 넘어오는 시간동안 기다려야 합니다
  // 이때 { name: name }과 { name }은 완전히 동일하게 동작합니다
  const res = await fetchGET(SERVER_HOST, path, { name });

  // 응답이 성공적으로 넘어오지 않는다면 false를 반환
  if (res.status !== 200) {
    return false;
  }

  // 서버의 응답으로 넘어온 Data에서 원하는 정보에 접근,
  const resData = res.data;
  const profile = resData.profile;

  // innerHTML 함수를 통해 DOM Element의 내용을 수정합니다
  document.querySelector("#fetch-name").innerHTML = profile.name;
  document.querySelector("#fetch-mbti").innerHTML = profile.mbti;
  document.querySelector("#fetch-github").innerHTML = profile.github;

  // 서버에서 받아온 Data로 DOM Element 내용 수정까지 완료했다면 true를 반환합니다
  return true;
}

// Footprint 조희를 위한 함수
// async라는 키워드를 function 앞에 명시해야, 함수 내에서 await를 사용할 수 있습니다
async function getFootprint(name) {
  // Footprint 조회를 위한 서버의 EndPoint
  const path = "/footprint";

  // 서버에 GET요청을 보내서 응답을 받습니다
  // 이때 서버에서 응답이 넘어오는데는 시간이 소요되고,
  // Javascript의 비동기적 흐름 때문에 await를 사용하여 응답이 넘어오는 시간동안 기다려야 합니다
  // 이때 { name: name }과 { name }은 완전히 동일하게 동작합니다
  const res = await fetchGET(SERVER_HOST, path, { name });

  // 응답이 성공적으로 넘어오지 않는다면 false를 반환
  if (res.status !== 200) {
    return false;
  }

  const resData = res.data;
  const messages = resData.messages; // messages는 메시지 내용이 담겨있는 배열입니다

  // 메시지를 담을 가장 큰 보드인 .board에 접근하고
  const footprintBoard = document.querySelector(".board");

  for (let i = 0; i < messages.length; i++) {
    // 각각의 message 내용을 HTML과 CSS가 적용되도록 알맞은 형태의 div 태그로
    // innerHTML을 사용하여 DOM에 추가합니다
    footprintBoard.innerHTML += `<div class="board-row">${messages[i]}</div>`;
  }

  // 여기까지 문제없이 메시지를 불러왔다면 true 반환
  return true;
}

// Footprint 전송을 위한 함수
// async라는 키워드를 function 앞에 명시해야, 함수 내에서 await를 사용할 수 있습니다
async function sendFootprint() {
  // Footprint 전송을 위한 서버의 EndPoint
  const path = "/footprint";

  // 메시지와 받는사람은 HTML에서 제공하는 기본 태그인 input 태그에 작성됩니다
  // 이때 input태그는 innerHTML이 아닌, value라는 속성으로 현재 값을 읽어올 수 있습니다
  // 쉽게 생각해서 <div></div> <span></span> 태그와 같이, 닫는 태그가 있다면 innerHTML이라고 생각하시면 됩니다 (모든 경우에 그런건 아닙니다)
  const message = document.querySelector(".message-content").value;
  const sender = document.querySelector(".message-sender").value;

  // POST요청은 GET 요청과 달리 Request Body라는 Javascript 객체 형태에 데이터를 담아서 요청하는데,
  // 서버에서는 content와 receiverName이라는 값을 달라고 요구하고 있습니다
  // 따라서 저희는 위에서 읽어온 message와 sender 정보를 Reqest Body에 담아서 서버에 POST 요청을 보냅니다
  const res = await fetchPOST(SERVER_HOST, path, {
    content: message,
    receiverName: sender,
  });

  // 메시지가 성공적으로 전송 되었다는 서버 응답이 오면,
  if (res.status === 200) {
    // 성공적으로 전송되었다는 메시지를 띄워주고
    alert("메시지를 성공적으로 전송하였습니다.");

    // location.href() 함수를 사용해서 새로고침을 합니다
    // 자기 자신에게 메시지를 보냈을 경우, 새로고침을 통해 메시지 내용을 갱신하기 위해 사용하였습니다
    location.reload();
  } else {
    // 서버에서 200번 응답이 넘어오지 않았다면
    // 메시지가 성공적으로 전송되지 못했다는 뜻이므로 에러 메시지를 띄워줍니다
    alert("메시지 전송에 실패하였습니다.");
  }
}

// window.onload = function() {...} 에서 ...에 작성된 코드는 웹 페이지가 랜더링 된 후에 수행됩니다

window.onload = function () {
  // 프로필 정보를 서버에서 받아와서 DOM을 업데이트 합니다.
  // 성공적으로 업데이트 됐다면 isGetProfileSuccess는 true, 아니면 false
  const isGetProfileSuccess = getProfileData(NAME);

  // 메시지를 서버에서 받아와서 DOM을 업데이트 합니다.
  // 성공적으로 업데이트 됐다면 isGetFootprintSuccess는 true, 아니면 false
  const isGetFootprintSuccess = getFootprint(NAME);

  // 프로필 조회와 Footprint 조회 중, 하나라도 실패하였다면 데이터 로딩에 실패했다는 에러 메시지를 띄워줍니다.
  if (!isGetProfileSuccess || !isGetFootprintSuccess) {
    alert("데이터 로딩에 실패하였습니다.");
  }

  // 아래 코드는 지금 이해하지 않으셔도 좋습니다
  // send 버튼이 클릭되었을 때, sendFoorprint() 함수를 호출하도록 eventListener를 연결하였습니다
  const sendButton = document.querySelector(".send-btn");
  sendButton.addEventListener("click", () => {
    sendFootprint();
  });
};
