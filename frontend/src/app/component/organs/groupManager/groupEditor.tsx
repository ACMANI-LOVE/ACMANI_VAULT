import { useContext, useEffect, useState } from "react"
import { ButtonComponent, FlexBox, FrameBox, LargeLabel } from "../../atoms/atoms"
import StateContext from "../../contexts/state"
import useDatePickerField from "../../hooks/useDatePickerField"

const GroupEditor = () => {
  const { groupState } = useContext(StateContext)

  const [current, setCurrent] = useState(new Date().toLocaleDateString())
  const [DatePickerField, dateString] = useDatePickerField({initialDate:current})
  useEffect(()=>setCurrent(dateString),[dateString])

  const handleClickAdd  = () => {groupState.setState("CONFIRM")}
  const handleClickBack = () => {groupState.setState("SELECT")}

  return (<FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"center"}>
    <FlexBox fx={8}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"center"}>
        <LargeLabel text={"Period:"}/>
        <FlexBox fx={3}>
          <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
          <DatePickerField/>
          </FrameBox>
        </FlexBox>
        <FlexBox fx={1}>
          <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
            <LargeLabel text={`to: ${dateString}`}/>
          </FrameBox>
        </FlexBox>
      </FrameBox>
    </FlexBox>
    <FlexBox fx={2}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
        <ButtonComponent label={"Add"}  textSize={"caption"} btnType={"contained"} onClick={handleClickAdd }/>
        <ButtonComponent label={"Back"} textSize={"caption"} btnType={"contained"} onClick={handleClickBack}/>
      </FrameBox>
    </FlexBox>
  </FrameBox>)
}

export default GroupEditor