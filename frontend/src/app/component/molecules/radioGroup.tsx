import { FormControl, FormControlLabel, Radio, RadioGroup } from "@mui/material"
import { BaseSyntheticEvent } from "react"
import { FrameBox } from "../atoms/atoms"

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