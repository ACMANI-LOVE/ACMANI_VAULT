import { TextField } from "@mui/material"
import { BaseSyntheticEvent, ReactNode, useCallback, useState } from "react"
import { FrameBox } from "../atoms/atoms"

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
    return (<FrameBox direction={"row"} width={"100%"}>
      <TextField fullWidth value={counterValue} onChange={handleChangeValue} type={"number"} slotProps={{
        inputLabel: {
          shrink: true,
        },
      }}/>
    </FrameBox>)
  },[counterValue])
  return [CounterField, counterValue] as CounterFieldReturns
}

export default useCounterField