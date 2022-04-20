import { fetchGET, fetchPOST } from "./dataFetching.js";

const SERVER_HOST =
  "https://asia-northeast3-likelion-js-practice.cloudfunctions.net/api";

async function getProfileData(name) {
  const path = "/member";

  const res = await fetchGET(SERVER_HOST, path, { name });
  const resData = res.data;
  const profile = resData.profile;

  document.querySelector("#fetch-name").innerHTML = profile.name;
  document.querySelector("#fetch-mbti").innerHTML = profile.mbti;
  document.querySelector("#fetch-github").innerHTML = profile.github;
}

window.onload = () => {
  // 웹 페이지의 모든 element(HTML, CSS)가 화면에 띄워지면 실행됩니다.
  console.log("page load!");

  // 프로필 정보를 서버에서 받아와서 업데이트 합니다.
  getProfileData("김영권");
};
