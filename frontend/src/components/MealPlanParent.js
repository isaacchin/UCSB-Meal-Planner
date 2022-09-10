import { MealPicker } from "./MenuPicker";
import { MenuChecklist } from "./MenuChecklist";
import React, { useState } from "react";

export const MealPlanParent = () => {

    const [readyToRenderChecklist, updateChecklistStatus] = useState(false);
    const [fooditems, setFoodItems] = useState([]);

    const handleStatusCallback = (menuPickerData) => {
        updateChecklistStatus(menuPickerData);
    }

    const handleMenuCallback = (menuPickerData) => {
        setFoodItems(menuPickerData);
        // console.log(fooditems);
    }

    return (
        <div>
            <MealPicker parentRenderCallback = {handleStatusCallback} parentMenuCallback = {handleMenuCallback}/>
            <>{readyToRenderChecklist ? <MenuChecklist menu = {fooditems}/> : null}</>
        </div>
    )
}