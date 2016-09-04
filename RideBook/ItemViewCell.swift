//
//  ItemViewCell.swift
//  RideBook
//
//  Created by hupei on 16/5/28.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit

class ItemViewCell: UITableViewCell {

    @IBOutlet weak var itemDesc: UILabel!
    @IBOutlet weak var itemRank: UILabel!
    @IBOutlet weak var itemRankSlider: UISlider!
    @IBOutlet weak var itemRemark: UITextField!
    
    @IBAction func Add(sender: AnyObject) {
        
    }
    
    @IBAction func RankSliderMove(sender: AnyObject) {
        
        let v=itemRankSlider.value
        let a=lroundf(v*10)
        let b=Float(lroundf(Float(a)*0.2))/2.0
        
        itemRank.text="\(b)"
    }
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }
    
}
