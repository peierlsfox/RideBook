//
//  VehicleViewCell.swift
//  RideBook
//
//  Created by hupei on 16/5/30.
//  Copyright © 2016年 hupei. All rights reserved.
//

import UIKit

class VehicleViewCell: UITableViewCell {

    @IBOutlet weak var detailLabel: UILabel!
    @IBOutlet weak var noLabel: UILabel!
    @IBOutlet weak var descLabel: UILabel!
    @IBOutlet weak var vehicleImage: UIView!
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
