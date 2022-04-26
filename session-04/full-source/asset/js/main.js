import { fetchGET, fetchPOST } from "./dataFetching.js";

const SERVER_HOST =
  "https://asia-northeast3-likelion-js-practice.cloudfunctions.net/api";

const NAME = "김영권";

async function getProfileData(name) {
  const path = "/member";

  const res = await fetchGET(SERVER_HOST, path, { name });
  const resData = res.data;
  const profile = resData.profile;

  document.querySelector("#fetch-name").innerHTML = profile.name;
  document.querySelector("#fetch-mbti").innerHTML = profile.mbti;
  document.querySelector("#fetch-github").innerHTML = profile.github;
}

async function getFootprint(name) {
  const path = "/message";

  const res = await fetchGET(SERVER_HOST, path, { name });
  const resData = res.data;
  const messages = resData.messages;
  const footprintBoard = document.querySelector(".board");
  footprintBoard.innerHTML = "";

  messages.forEach((m) => {
    footprintBoard.innerHTML += `<div class="board-row">${m}</div>`;
  });
}

async function sendFootprint() {
  const path = "/message";

  const message = document.querySelector(".message-content").value;
  const sender = document.querySelector(".message-sender").value;

  const res = await fetchPOST(SERVER_HOST, path, {
    content: message,
    receiverName: sender,
  });

  if (res.status === 200) {
    alert("메시지를 성공적으로 전송하였습니다.");
  }
}

// 프로필 정보를 서버에서 받아와서 DOM을 업데이트 합니다.
getProfileData(NAME);

// 메시지를 서버에서 받아와서 DOM을 업데이트 합니다.
getFootprint(NAME);
