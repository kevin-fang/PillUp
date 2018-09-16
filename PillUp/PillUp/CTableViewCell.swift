//
//  TableView.swift
//  PillUp
//
//  Created by Shayan on 9/16/18.
//  Copyright © 2018 Shayan. All rights reserved.
//

import Foundation
import UIKit

class CTableViewCell: UITableViewCell {
    
    var iconView: UIImageView!
    var title: UILabel!
    var desc: UILabel!
    var time: UILabel!
    var button: UIButton!
    
    override init(style: UITableViewCellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        
        iconView = UIImageView()
        title = UILabel()
        desc = UILabel()
        time = UILabel()
        button = UIButton()
        
        self.addSubview(iconView)
        self.addSubview(title)
        self.addSubview(desc)
        self.addSubview(time)
        self.addSubview(button)
        
        iconView.snp.makeConstraints { make in
            make.left.equalTo(25)
            make.centerY.equalToSuperview()
            make.height.width.equalTo(33)
        }
        
        title.snp.makeConstraints { make in
            make.left.equalTo(iconView.snp.right).offset(13)
            make.top.equalToSuperview().offset(20)
        }
        
        desc.snp.makeConstraints { make in
            make.left.equalTo(title.snp.left)
            make.top.equalTo(title.snp.bottom)
        }
        
        time.snp.makeConstraints { make in
            make.right.equalToSuperview().offset(-25)
            make.centerY.equalTo(title)
        }
        
        button.snp.makeConstraints { make in
            make.right.equalTo(time.snp.right)
            make.width.equalTo(70)
            make.centerY.equalTo(desc.snp.centerY)
        }
        
        button.imageView?.contentMode = .scaleAspectFit
        
        iconView.clipsToBounds = true
        iconView.contentMode = .scaleAspectFit
        title.font = UIFont.systemFont(ofSize: 20, weight: .medium)
        desc.font = UIFont.systemFont(ofSize: 12, weight: .medium)
        time.font = UIFont.systemFont(ofSize: 13, weight: .thin)
    
        time.textAlignment = .right
        
        self.selectedBackgroundView?.backgroundColor = .clear
        self.backgroundColor = .clear
        
        let view = UIView()
        self.addSubview(view)
        view.snp.makeConstraints { make in
            make.left.bottom.right.equalToSuperview()
            make.height.equalTo(0.3)
        }
        view.backgroundColor = .black
        view.alpha = 0.3
        
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setup(title: String, desc: String, time: String, image: UIImage) {
        
        self.title.text = title
        self.desc.text = desc
        self.time.text = time
        self.iconView.image = image
        
    }
    

    
    
}
