import { Components } from "@/const/type"
import { FrameBox, FlexBox } from "../atoms/atoms"
import AppBarComponent from "../organs/appFrame/appBar"
import SideMenuComponent from "../organs/appFrame/sideMenu"

interface AppFrameProps {
  children: Components
}
const AppFrame = ({children}:AppFrameProps) => {
  return (<FrameBox height={"100%"} direction={"column"}>
    <AppBarComponent/>
    <FrameBox height={"100%"} direction={"row"}>
      <SideMenuComponent/>
      <FlexBox fx={1}>
        {children}
      </FlexBox>
    </FrameBox>
  </FrameBox>)
}

export default AppFrame