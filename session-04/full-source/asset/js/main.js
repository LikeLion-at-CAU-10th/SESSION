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
