<template>
  <input
    :type="type"
    :value="internalValue"
    @input="updateInternalValue"
  />
</template>

<script>
import _debounce from 'lodash/debounce'

export default {
  props: {
    value: String,
    type: { type: String, default: 'text' },
    delay: {type: Number, default: 500 },
  },
  data () {
    return {
      internalValue: this.value,
      touched: false,
    }
  },
  watch: {
    value (value) {
      if (!this.touched) this.internalValue = value
    },
  },
  methods: {
    updateInternalValue (event) {
      this.touched = true
      this.updateValue(event.target.value)
    },
    updateValue: _debounce(function (value) {
      this.touched = false
      this.$emit('input', value)
      this.$emit('update:value', value)
    }, 2000),
  },
}
</script>