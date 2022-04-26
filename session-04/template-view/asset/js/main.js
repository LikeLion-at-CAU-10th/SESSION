import { fetchGET, fetchPOST } from "./dataFetching.js";

const SERVER_HOST =
  "https://asia-northeast3-likelion-js-practice.cloudfunctions.net/api";

const NAME = "김영권";

async function getProfileData(name) {}

async function getFootprint(name) {}

async function sendFootprint() {}

window.onload = function () {
  const sendButton = document.querySelector(".send-btn");
  sendButton.addEventListener("click", () => {
    sendFootprint();
  });
};
