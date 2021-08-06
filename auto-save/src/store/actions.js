import ApiCall from "../js/api.js";

export default {
  callAPI: async ({ commit }, payload) => {
    console.log("calling API now!");
    await ApiCall(payload);
    commit("CALL_API");
  },
  setSaving: ({ commit }, payload) => {
    commit("SET_SAVING", payload);
  },
};
