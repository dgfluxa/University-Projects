# frozen_string_literal: true

require 'test_helper'

class ModeratedCoursesControllerTest < ActionDispatch::IntegrationTest
  test 'should get update' do
    get moderated_courses_update_url
    assert_response :success
  end
end
