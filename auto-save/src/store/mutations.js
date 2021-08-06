import { MESSAGES } from "../js/constants";
export default {
  SET_SAVING: (state, payload) => {
    state.saving.msg = MESSAGES.SAVING;
    state.saving.show = payload;
  },
  CALL_API: (state) => {
    state.saving.msg = MESSAGES.SAVED;
  },
};
