import { TextField } from "@mui/material"
import { ReactNode, useState, useCallback, BaseSyntheticEvent } from "react"

interface CounterFieldProps {
  initialValue: number
}
type CounterFieldReturns = [
  CounterField: ()=>ReactNode,
  counterValue: number
]
const useCounterField = ({initialValue}:CounterFieldProps) => {
  const [counterValue, setCounterValue] = useState(initialValue)
  const CounterField = useCallback(()=>{
    const handleChangeValue = (e:BaseSyntheticEvent) => setCounterValue(Number(e.target.value))
    return (
    <TextField value={counterValue} onChange={handleChangeValue} type={"number"} slotProps={{
      inputLabel: {
        shrink: true,
      },
    }}/>)
  },[counterValue])
  return [CounterField, counterValue] as CounterFieldReturns
}

export default useCounterField