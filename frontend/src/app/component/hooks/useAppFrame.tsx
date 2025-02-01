import { ReactNode, useState } from "react";
import AppBarComponent from "../organs/appBar";
import SideMenuComponent from "../organs/sideMenu";

interface AppFrameProps {}

type AppFrameReturns = [
  AppBar:   ()=>ReactNode,
  SideMenu: ()=>ReactNode,
  openMenu:    boolean,
]

const useAppFrame = ({}:AppFrameProps):AppFrameReturns => {

  const [menuFlg, setMenuFlg] = useState(false)

  const clickMenuButton = () => setMenuFlg(!menuFlg)

  const AppBar = () => <AppBarComponent onClickMenu={clickMenuButton}/>

  const SideMenu = () => <SideMenuComponent open={menuFlg}/>

  return [AppBar, SideMenu, menuFlg] as AppFrameReturns
}

export default useAppFrame
