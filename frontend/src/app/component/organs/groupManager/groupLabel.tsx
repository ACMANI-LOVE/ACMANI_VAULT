import { useContext } from "react"
import { ButtonComponent, FlexBox, FrameBox, LargeLabel } from "../../atoms/atoms"
import DataContext from "../../contexts/data"
import StateContext from "../../contexts/state"

const GroupLabel  = () => {
  const { groupState } = useContext(StateContext)
  const { group } = useContext(DataContext)

  const handleClickChange = () => {groupState.setState("SELECT")}
  const handleClickDelete = () => {groupState.setState("SELECT")}

  return (<FrameBox direction={"row"} padding={"0.25em"} width={"100%"} align={"center"} justify={"center"}>
    <FlexBox fx={8}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"center"}>
        <LargeLabel text={"Period:"}/>
        <FlexBox fx={1}>
          <LargeLabel text={group.state.name}/>
        </FlexBox>
      </FrameBox>
    </FlexBox>
    <FlexBox fx={2}>
      <FrameBox direction={"row"} width={"100%"} align={"center"} justify={"space-around"}>
        <ButtonComponent label={"Change"} textSize={"caption"} btnType={"contained"} onClick={handleClickChange}/>
        <ButtonComponent label={"Delete"} textSize={"caption"} btnType={"contained"} onClick={handleClickDelete}/>
      </FrameBox>
    </FlexBox>
  </FrameBox>)
}

export default GroupLabel