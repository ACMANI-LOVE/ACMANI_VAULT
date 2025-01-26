import { FormControl, RadioGroup, FormControlLabel, Radio } from "@mui/material"
import { FrameBox } from "../atomos/atomos"
import { BaseSyntheticEvent } from "react"

interface SelectorProps {
  list:     string[]
  select:  number
  onChange: (e:BaseSyntheticEvent) => void

}

const Selector = ({list, select, onChange}:SelectorProps) => {
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

export default Selector