import { FormControl, RadioGroup, FormControlLabel, Radio } from "@mui/material"
import { FrameBox } from "../atoms/atoms"
import { BaseSyntheticEvent } from "react"

interface RadioListProps {
  list:     string[]
  select:  number
  onChange: (e:BaseSyntheticEvent) => void
}

const RadioList = ({list, select, onChange}:RadioListProps) => {
  return (<FrameBox padding={"0.1em"} direction={"column"}>
    <FormControl>
      <RadioGroup defaultValue={select} onChange={onChange}>
        {list.map((item,idx)=><FormControlLabel
          key={idx}
          value={idx}
          label={item}
          control={<Radio size={"small"}/>}
          />)}
      </RadioGroup>
    </FormControl>
  </FrameBox>)
}

export default RadioList