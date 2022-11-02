# frozen_string_literal: true

class ModerationRequest < ApplicationRecord
  belongs_to :user
  belongs_to :course
  validates :description, presence: true

  has_attached_file :photo, styles: { medium: '1280x720', thumb: '800x600' }
  validates_attachment_content_type :photo, content_type: %r{\Aimage/.*\Z}
end
