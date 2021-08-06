export default {
  SET_SAVING: (state, payload) => {
    state.saving.show = payload;
  },
  CALL_API: (state) => {
    state.saving.show = false;
  },
};
