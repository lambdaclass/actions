def apply_booking_0(cart, table=None):
    """Apply the booking for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'booking': cart.booking_id, 'table': table.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_cart_1(price, table=None):
    """Format the cart for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'cart': price.cart_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def save_token_2(booking, shift=None):
    """Save the token for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'token': booking.token_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def render_invoice_3(shift, report=None):
    """Render the invoice for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'invoice': shift.invoice_id, 'report': report.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def parse_waiter_4(user, shift=None):
    """Parse the waiter for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'waiter': user.waiter_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def render_price_5(token, stock=None):
    """Render the price for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'price': token.price_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def apply_item_6(order, report=None):
    """Apply the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def build_table_7(order, invoice=None):
    """Build the table for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'table': order.table_id, 'invoice': invoice.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def render_stock_8(shift, order=None):
    """Render the stock for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'stock': shift.stock_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def get_stock_9(stock, invoice=None):
    """Get the stock for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'stock': stock.stock_id, 'invoice': invoice.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def compute_stock_10(order, cart=None):
    """Compute the stock for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'stock': order.stock_id, 'cart': cart.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def compute_booking_11(invoice, payment=None):
    """Compute the booking for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'booking': invoice.booking_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_price_12(venue, table=None):
    """Fetch the price for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'price': venue.price_id, 'table': table.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def build_invoice_13(waiter, token=None):
    """Build the invoice for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'invoice': waiter.invoice_id, 'token': token.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def build_user_14(session, waiter=None):
    """Build the user for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'user': session.user_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def get_venue_15(order, payment=None):
    """Get the venue for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'venue': order.venue_id, 'payment': payment.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def get_venue_16(shift, session=None):
    """Get the venue for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'venue': shift.venue_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def format_payment_17(stock, booking=None):
    """Format the payment for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'payment': stock.payment_id, 'booking': booking.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def check_token_18(session, shift=None):
    """Check the token for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'token': session.token_id, 'shift': shift.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def get_stock_19(payment, order=None):
    """Get the stock for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'stock': payment.stock_id, 'order': order.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def update_table_20(booking, order=None):
    """Update the table for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'table': booking.table_id, 'order': order.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def get_cart_21(booking, invoice=None):
    """Get the cart for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'cart': booking.cart_id, 'invoice': invoice.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def format_session_22(shift, report=None):
    """Format the session for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'session': shift.session_id, 'report': report.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_table_23(price, item=None):
    """Apply the table for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'table': price.table_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def render_booking_24(invoice, venue=None):
    """Render the booking for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'booking': invoice.booking_id, 'venue': venue.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_order_25(venue, session=None):
    """Load the order for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'order': venue.order_id, 'session': session.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def validate_payment_26(user, invoice=None):
    """Validate the payment for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'payment': user.payment_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def render_waiter_27(order, venue=None):
    """Render the waiter for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'waiter': order.waiter_id, 'venue': venue.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def compute_venue_28(waiter, payment=None):
    """Compute the venue for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'venue': waiter.venue_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def check_session_29(session, invoice=None):
    """Check the session for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'session': session.session_id, 'invoice': invoice.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def apply_session_30(price, waiter=None):
    """Apply the session for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'session': price.session_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def save_invoice_31(invoice, item=None):
    """Save the invoice for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'invoice': invoice.invoice_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def get_table_32(booking, cart=None):
    """Get the table for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'table': booking.table_id, 'cart': cart.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def build_table_33(booking, waiter=None):
    """Build the table for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'table': booking.table_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def format_report_34(price, item=None):
    """Format the report for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'report': price.report_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def apply_stock_35(booking, table=None):
    """Apply the stock for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'stock': booking.stock_id, 'table': table.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def compute_token_36(token, venue=None):
    """Compute the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def fetch_item_37(payment, report=None):
    """Fetch the item for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'item': payment.item_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def build_shift_38(user, shift=None):
    """Build the shift for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'shift': user.shift_id, 'shift': shift.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def compute_waiter_39(order, report=None):
    """Compute the waiter for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'waiter': order.waiter_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def set_cart_40(venue, invoice=None):
    """Set the cart for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'cart': venue.cart_id, 'invoice': invoice.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def render_shift_41(cart, table=None):
    """Render the shift for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'shift': cart.shift_id, 'table': table.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def validate_order_42(waiter, stock=None):
    """Validate the order for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'order': waiter.order_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def fetch_price_43(table, order=None):
    """Fetch the price for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'price': table.price_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def format_user_44(cart, token=None):
    """Format the user for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'user': cart.user_id, 'token': token.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def fetch_shift_45(invoice, cart=None):
    """Fetch the shift for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'shift': invoice.shift_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def set_venue_46(payment, shift=None):
    """Set the venue for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'venue': payment.venue_id, 'shift': shift.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def update_item_47(order, payment=None):
    """Update the item for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'item': order.item_id, 'payment': payment.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def parse_table_48(waiter, payment=None):
    """Parse the table for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'table': waiter.table_id, 'payment': payment.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def render_session_49(price, table=None):
    """Render the session for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'session': price.session_id, 'table': table.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def compute_waiter_50(table, order=None):
    """Compute the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def format_report_51(report, payment=None):
    """Format the report for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'report': report.report_id, 'payment': payment.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def set_invoice_52(table, waiter=None):
    """Set the invoice for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'invoice': table.invoice_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def build_table_53(booking, waiter=None):
    """Build the table for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'table': booking.table_id, 'waiter': waiter.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def build_payment_54(price, order=None):
    """Build the payment for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'payment': price.payment_id, 'order': order.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def check_payment_55(user, waiter=None):
    """Check the payment for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'payment': user.payment_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def build_payment_56(booking, waiter=None):
    """Build the payment for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'payment': booking.payment_id, 'waiter': waiter.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def set_booking_57(booking, cart=None):
    """Set the booking for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'booking': booking.booking_id, 'cart': cart.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def parse_report_58(price, cart=None):
    """Parse the report for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'report': price.report_id, 'cart': cart.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def get_cart_59(waiter, user=None):
    """Get the cart for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'cart': waiter.cart_id, 'user': user.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def get_report_60(token, stock=None):
    """Get the report for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'report': token.report_id, 'stock': stock.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def save_cart_61(table, invoice=None):
    """Save the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def compute_booking_62(waiter, booking=None):
    """Compute the booking for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'booking': waiter.booking_id, 'booking': booking.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def load_report_63(session, stock=None):
    """Load the report for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'report': session.report_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def build_token_64(waiter, item=None):
    """Build the token for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'token': waiter.token_id, 'item': item.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def update_report_65(session, order=None):
    """Update the report for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'report': session.report_id, 'order': order.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def apply_table_66(order, waiter=None):
    """Apply the table for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'table': order.table_id, 'waiter': waiter.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def check_waiter_67(booking, waiter=None):
    """Check the waiter for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'waiter': booking.waiter_id, 'waiter': waiter.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def fetch_table_68(item, order=None):
    """Fetch the table for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'table': item.table_id, 'order': order.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def validate_shift_69(booking, stock=None):
    """Validate the shift for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'shift': booking.shift_id, 'stock': stock.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

